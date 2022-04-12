
# 1) Message @BotFather, follow prompts
# 2) Make channel and invite your bot
# 3) Invite @RawDataBot for your chat ID, then kick it out

import logging
import telebot
from config import TG_TOKEN, TG_CHAT_ID, TG_INSTANCE_NAME
logger = logging.getLogger('VXX Flipper')


class TG_bot:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.bot = telebot.TeleBot(TG_TOKEN)
        # self.stats = False


    def sendTelegramMessage(self, message, instance_name=TG_INSTANCE_NAME):
        try:
            message_instanced = "*{}*\n{}".format(instance_name, message)
            self.bot.send_message(TG_CHAT_ID, message_instanced, parse_mode='Markdown')
        except Exception as ex:
            logger.error("TG Sending error {}".format(ex))