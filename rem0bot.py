import logging
import os
import telegram
from setup_logging import setup_logging
from telegram.ext import Updater, CommandHandler

setup_logging()
logger = logging.getLogger(__name__)

token = os.environ['rem0bot_token']

bot = telegram.Bot(token=token)
logger.debug(bot.get_me())

updater = Updater(token=token)
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id, text='Hello, I am rem0bot!')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
