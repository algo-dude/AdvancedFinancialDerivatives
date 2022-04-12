
# 1) Message @BotFather, follow prompts
# 2) Make channel and invite your bot
# 3) Invite @RawDataBot for your chat ID, then kick it out

import logging
import telebot
from threading import Thread
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


    def generate_bot(self):
        interval = 5
        timeout = 60
        self.thx = Thread(target=self.bot.infinity_polling, args=(interval, timeout))

    def poll_data(self):
        logger.info("Polling TG data")
        try:
            if not self.thx.is_alive():
                self.thx.start()
        except Exception as ex:
            print(ex)
            logger.error("TG pool data error {}".format(ex))


    def sendTelegramMessage(self, message, instance_name=TG_INSTANCE_NAME):
        try:
            message_instanced = "VXX Flipper *{}*\n{}".format(instance_name, message)
            self.bot.send_message(TG_CHAT_ID, message_instanced, parse_mode='Markdown')
        except Exception as ex:
            logger.error("TG Sending error {}".format(ex))