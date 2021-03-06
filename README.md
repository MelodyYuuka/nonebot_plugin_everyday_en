<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# nonebot_plugin_everyday_en

ð¥éç¨äº [Nonebot2](https://github.com/nonebot/nonebot2) çæ¯æ¥ä¸å¥æä»¶ð¥
  
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

## å®è£è½½å¥

- éè¿ pip æ nb-cli å®è£

```shell
pip install nonebot-plugin-everyday-en
```

- å¹¶å¨æ¨çbot.pyä¸­è½½å¥æä»¶

```python
nonebot.load_plugin("nonebot_plugin_everyday_en")
```

- å¦éä½¿ç¨å®æ¶åéåè½ï¼è¿éå®è£è½¯ä¾èµ [nonebot-plugin-apscheduler](https://github.com/nonebot/plugin-apscheduler)
```shell
pip install nonebot-plugin-apscheduler
```

## æä»¤
- `æ¯æ¥ä¸å¥`: è·åä»å¤©çå¥å­
  - `æ¯æ¥ä¸å¥[æ¥æ]`: è·åæå®æ¥æçå¥å­
    > æ¥ææ ¼å¼ä¸º YYYY-MM-DD , ä¾å¦ 2020-01-08

- `å¼å¯/å³é­å®æ¶æ¯æ¥ä¸å¥`: å¼å¯/å³é­æ¬ç¾¤å®æ¶åé **[SUPERUSER]**
  - `å¼å¯/å³é­å®æ¶æ¯æ¥ä¸å¥[ç¾¤å·]`: å¼å¯/å³é­æå®ç¾¤å®æ¶åé **[SUPERUSER]**

- `æ¥çå®æ¶æ¯æ¥ä¸å¥åè¡¨`: ååºå¼å¯å®æ¶åéçç¾¤è **[SUPERUSER]**

## éç½®é¡¹

éç½®æ¹å¼ï¼ç´æ¥å¨ NoneBot å¨å±éç½®æä»¶ä¸­æ·»å ä»¥ä¸éç½®é¡¹å³å¯ã

NoneBot éç½®ç¸å³æç¨è¯¦è§ [éç½® | NoneBot](https://v2.nonebot.dev/docs/tutorial/configuration)

ð¢ é»è®¤éç½®ä¸ºæ¯æ¥ 8:00 åé
### everyday_post_hour
- ç±»å: int
- é»è®¤: 8
- è¯´æ: æ¯æ¥å®æ¶åéçå°æ¶ï¼ä¸éè¦å¨æ°å­åå 0
>```python
>EVERYDAY_POST_HOUR=8
>```

### everyday_post_minute
- ç±»å: int
- é»è®¤: 0
- è¯´æ: æ¯æ¥å®æ¶åéçåéï¼ä¸éè¦å¨æ°å­åå 0
>```python
>EVERYDAY_POST_MINUTE=0
>```

### everyday_delay
- ç±»å: float
- é»è®¤: 0.5
- è¯´æ: å®æ¶åéæ¶åç¾¤é´åéçå»¶è¿ç§æ°ï¼ä»¥åè¾è®¯é£æ§å¯¼è´åéå¤±è´¥
>```python
>EVERYDAY_DELAY=0.5
>```

## è½¯ä¾èµ
- [`nonebot-plugin-apscheduler`](https://github.com/nonebot/plugin-apscheduler): ä½¿ç¨å®æ¶åéåè½

- [`nonebot-plugin-help`](https://github.com/XZhouQD/nonebot-plugin-help): å¨ç¾¤åæ¥çå¸®å©ææ¡£
  - ä¹å¯èªè¡è§£æ `__help_plugin_name__` , `__help_version__` , `__usage__`æ¥æ¥å¥æ¨èªå·±çå¸®å©æä»¶

## å¸¸è§é®é¢

### `Q: ä¸ºä»ä¹æ²¡æè¯­é³ï¼`
- A: å¦æä½ ä½¿ç¨çæ¯`go-cqhttp`ï¼é£ä¹ä½ éè¦å®è£`FFmpeg`å¹¶éå¯æ¬æä»¶æ¥ä½¿ç¨è¯­é³åè½ï¼è¯¦è§[`å®è£ ffmpeg`](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%AE%89%E8%A3%85-ffmpeg)

### `Q: ä¸ºä»ä¹å®æ¶åéæ¯æ¥ä¸å¥æäºç¾¤æ æ³æ¶å°ï¼`
- A: æ£æ¥æ¥å¿ï¼é¢ç¹åéæ¶æ¯å¯è½å¯¼è´è¾è®¯é£æ§ï¼å¯éè¿è®¾ç½®[`everyday_delay`](https://github.com/MelodyYuuka/nonebot_plugin_everyday_en#everyday_delay)éç½®é¡¹è®¾ç½®åéå»¶è¿æ¥ç¼è§£

## å¼æºè®¸å¯

- æ¬æä»¶ä½¿ç¨ `MIT` è®¸å¯è¯å¼æº
