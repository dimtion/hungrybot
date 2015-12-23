HungryBot
=========

HungryBot is a simple bot for Slack that parse's the RAK's menu.

# Installation process

## Requirements :
pip install websockets-client

## WHAT TODO :
create a configuration file:
```
cp config.py.tpl config.py
```

Insert your token into the config file

Insert this in the crontab (crontab -e) :
```
30 10 * * * cd /whereever/hungrybot && python2 bot.py 0
30 18 * * * cd /whereever/hungrybot && python2 bot.py 1
00 22 * * 0 cd /whereever/hungrybot && python2 majDb.py
```
