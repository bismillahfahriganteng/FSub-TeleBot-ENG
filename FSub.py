import logging
from pyrogram import Client
from config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="plugins",
    include=[
        "forceSubscribe",
        "help"
    ]
)

app = Client(
     'ForceSubscribe',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      updates_ch = Config.UPDATES_CH,
      support_grp = Config.SUPPORT_GRP,
      updates_name = Config.UPDATES_NAME,
      support_name = Config.SUPPORT_NAME,
      plugins = plugins
)

app.run()
