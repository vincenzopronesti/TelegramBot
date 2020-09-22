import configparser
from telegram.ext import Updater, CommandHandler
import logging
from telegram import ChatAction
import time

config = configparser.ConfigParser()
config.read('bot.ini')

updater = Updater(token = config['KEYS']['bot_api'])
dispatcher = updater.dispatcher

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level = logging.INFO)

def start(bot, update):
	if update.message.from_user.id == int(config['ADMIN']['id']):
		bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		time.sleep(1)
		bot.send_message(chat_id = update.message.chat_id, text = "I'm a bot, please, talk to me!")
	else:
		bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		time.sleep(1)
		bot.sendMessage(chat_id=update.message.chat_id, text="It seems like you aren't allowed to use me. :(")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

from telegram.ext import MessageHandler, Filters

def echo(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = '  '.join(args).upper()
    bot.send_message(chat_id = update.message.chat_id, text = text_caps)

caps_handler = CommandHandler('caps', caps, pass_args = True)
dispatcher.add_handler(caps_handler)

def unknown(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.idle()
