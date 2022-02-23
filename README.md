<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# nonebot_plugin_everyday_en

🍥适用于 [Nonebot2](https://github.com/nonebot/nonebot2) 的每日一句插件🍥
  
</div>

<p align="center">
  
  <a href="https://raw.githubusercontent.com/MelodyYuuka/nonebot_plugin_everyday_en/master/LICENSE">
    <img src="https://img.shields.io/github/license/MelodyYuuka/nonebot_plugin_everyday_en" alt="license">
  </a>

  <a href="https://pypi.python.org/pypi/nonebot_plugin_everyday_en">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_everyday_en" alt="pypi">
  </a>

  <a href="https://onebot.dev">
    <img src="https://img.shields.io/badge/OneBot-11-black" alt="license">
  </a>
  
  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot2-2.0.0beta.1+-green">
  </a>
  
  <a href="">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="python">
  </a>
  
</p>

## 安装载入

- 通过 pip 或 nb-cli 安装

```shell
pip install nonebot-plugin-everyday-en
```

- 并在您的bot.py中载入插件

```python
nonebot.load_plugin("nonebot_plugin_everyday_en")
```

- 如需使用定时发送功能，还需安装软依赖 [nonebot_plugin_apscheduler](https://github.com/nonebot/plugin-apscheduler)
```shell
pip install nonebot-plugin-apscheduler
```

## 指令
- `每日一句`: 获取今天的句子
  - `每日一句[日期]`: 获取指定日期的句子
    > 日期格式为 YYYY-MM-DD , 例如 2020-01-08

- `开启/关闭定时每日一句`: 开启/关闭本群定时发送 **[SUPERUSER]**
  - `开启/关闭定时每日一句[群号]`: 开启/关闭指定群定时发送 **[SUPERUSER]**

- `查看定时每日一句列表`: 列出开启定时发送的群聊 **[SUPERUSER]**

## 配置项

配置方式：直接在 NoneBot 全局配置文件中添加以下配置项即可。

NoneBot 配置相关教程详见 [配置 | NoneBot](https://v2.nonebot.dev/docs/tutorial/configuration)

🟢 默认配置为每日 8:00 发送
### everyday_post_hour
- 类型: int
- 默认: 8
- 说明: 每日定时发送的小时，不需要在数字前加0
>```python
>EVERYDAY_POST_HOUR=8
>```

### everyday_post_minute
- 类型: int
- 默认: 0
- 说明: 每日定时发送的分钟，不需要在数字前加0
>```python
>EVERYDAY_POST_MINUTE=0
>```

### everyday_delay
- 类型: float
- 默认: 0.5
- 说明: 定时发送时各群间发送的延迟秒数，以免腾讯风控导致发送失败
>```python
>EVERYDAY_DELAY=0.5
>```

## 软依赖
- [`nonebot_plugin_apscheduler`](https://github.com/nonebot/plugin-apscheduler): 使用定时发送功能

- [`nonebot-plugin-help`](https://github.com/XZhouQD/nonebot-plugin-help): 在群内查看帮助文档
  - 也可自行解析 `__help_plugin_name__` , `__help_version__` , `__usage__`来接入您自己的帮助插件

## 常见问题

### `Q: 为什么定时发送每日一句某些群无法收到`
- A: 检查日志，频繁发送消息可能导致腾讯风控，可通过设置[`everyday_delay`](https://github.com/MelodyYuuka/nonebot_plugin_everyday_en#everyday_delay)配置项设置发送延迟来缓解

## 开源许可

- 本插件使用 `MIT` 许可证开源
