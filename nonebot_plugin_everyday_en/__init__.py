from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
    MessageSegment,
    Message,
    GroupMessageEvent,
)
from nonebot.params import Matcher, RegexGroup
from nonebot.log import logger
from nonebot.permission import SUPERUSER
from nonebot import require, get_driver, get_bot
from typing import Dict, List, Optional, Tuple, Union
from pathlib import Path
from datetime import date
from textwrap import dedent
import asyncio
import aiofiles
import httpx
from .config import Config

try:
    import ujson as json
except ImportError:
    import json


__help_plugin_name__ = "每日一句"
__help_version__ = "1.0"
__usage__ = dedent(
    """每日一句 → 获取每日一句
       每日一句[日期] → 获取特定日期的句子
       [日期]形如YYYY-MM-DD, 例如2020-01-08
       开启/关闭定时每日一句 → 开启/关闭本群定时发送[SUPERUSER]
       开启/关闭定时每日一句[群号] → 开关指定群定时发送[SUPERUSER]
       查看定时每日一句列表 → 列出开启定时发送的群聊[SUPERUSER]"""
)

env_config = Config(**get_driver().config.dict())

config_path = Path("config/everyday_en.json")
config_path.parent.mkdir(parents=True, exist_ok=True)
if config_path.exists():
    with open(config_path, "r", encoding="utf8") as f:
        CONFIG: Dict[str, List] = json.load(f)
else:
    CONFIG: Dict[str, List] = {"opened_groups": []}
    with open(config_path, "w", encoding="utf8") as f:
        json.dump(CONFIG, f, ensure_ascii=False, indent=4)

try:
    scheduler = require("nonebot_plugin_apscheduler").scheduler
except BaseException:
    scheduler = None

logger.opt(colors=True).info(
    "已检测到软依赖<y>nonebot_plugin_apscheduler</y>, <g>开启定时任务功能</g>"
    if scheduler
    else "未检测到软依赖<y>nonebot_plugin_apscheduler</y>，<r>禁用定时任务功能</r>"
)

everyday_en_matcher = on_regex(r"^每日一句(\d{4}-\d{2}-\d{2})?$", priority=999)
turn_matcher = on_regex(r"^(开启|关闭)定时每日一句([0-9]*)$", priority=999, permission=SUPERUSER)
list_matcher = on_regex(r"^查看定时每日一句列表$", priority=999, permission=SUPERUSER)


data_cache: Dict = None
cache_time: date = None

lock = asyncio.Lock()


@everyday_en_matcher.handle()
async def _(
    bot: Bot,
    event: MessageEvent,
    matcher: Matcher,
    args: Tuple[Optional[str]] = RegexGroup(),
):
    query_date = args[0] if args[0] else None
    if cache_time != date.today() or (not data_cache) or args[0]:
        try:
            data = await get_data(query_date)
        except BaseException as e:
            logger.exception(e)
            await matcher.finish("发生了问题，可能是输入了错误日期或发生了网络错误")
    else:
        data = data_cache
    await matcher.send(MessageSegment.record(data["tts"]))
    msg = format_data(data)
    await matcher.finish(msg)


@turn_matcher.handle()
async def _(
    bot: Bot,
    event: MessageEvent,
    matcher: Matcher,
    args: Tuple[Optional[str], ...] = RegexGroup(),
):
    if not scheduler:
        await matcher.finish("未安装软依赖nonebot_plugin_apscheduler，不能使用定时发送功能")
    mode = args[0]
    if isinstance(event, GroupMessageEvent):
        group_id = args[1] if args[1] else str(event.group_id)
    else:
        group_id = args[1]
    if mode == "开启":
        if group_id in CONFIG["opened_groups"]:
            await matcher.finish("该群已经开启，无需重复开启")
        else:
            CONFIG["opened_groups"].append(group_id)
    else:
        if group_id in CONFIG["opened_groups"]:
            CONFIG["opened_groups"].remove(group_id)
        else:
            await matcher.finish("该群尚未开启，无需关闭")
    async with lock:
        async with aiofiles.open(config_path, "w", encoding="utf8") as f:
            await f.write(json.dumps(CONFIG, ensure_ascii=False, indent=4))
    await matcher.finish(
        f"已成功{mode}{(await bot.get_group_info(group_id=int(group_id)))['group_name']}({group_id})每日一句"
    )


@list_matcher.handle()
async def _(bot: Bot, event: MessageEvent, matcher: Matcher):
    if not scheduler:
        await matcher.finish("未安装软依赖nonebot_plugin_apscheduler，不能使用定时发送功能")
    msg = "当前打开定时每日一句的群聊有：\n"
    for group_id in CONFIG["opened_groups"]:
        msg += f"{group_id}\n"
    await matcher.finish(msg.strip())


async def get_data(query_date: Optional[str] = None) -> Dict:
    global data_cache, cache_time
    params = {"date": query_date} if query_date else {"date": ""}
    async with httpx.AsyncClient() as client:
        data = (
            await client.get(
                "http://open.iciba.com/dsapi", params=params, follow_redirects=True
            )
        ).json()
    data_cache = data_cache if query_date else data
    cache_time = cache_time if query_date else date.today()
    return data


def format_data(data: Dict) -> Message:
    msg = MessageSegment.text(f"【{data['dateline']}】\n")
    msg += MessageSegment.image(data["picture4"])
    msg += MessageSegment.text(f"{data['content']}\n释义：{data['note']}")
    return msg


async def post_scheduler():
    if cache_time != date.today() or (not data_cache):
        data = await get_data()
    else:
        data = data_cache
    record = MessageSegment.record(data["tts"])
    msg = format_data(data)
    bot: Bot = get_bot()
    for group_id in CONFIG["opened_groups"]:
        await bot.send_group_msg(group_id=int(group_id), message=record)
        await bot.send_group_msg(group_id=int(group_id), message=msg)
        await asyncio.sleep(0.2)


if scheduler:
    hour = env_config.everyday_post_hour
    minute = env_config.everyday_post_minute
    logger.opt(colors=True).info(
        f"已设定于 <y>{str(hour).rjust(2, '0')}:{str(minute).rjust(2, '0')}</y> 定时发送每日一句"
    )
    scheduler.add_job(
        post_scheduler, "cron", hour=hour, minute=minute, id="everyday_english"
    )
