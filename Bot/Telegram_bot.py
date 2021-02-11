import os

import telegram
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from translater.main import main as translate

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telegram.Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='I am an interpreter bot, send me a text '
             'and i will will translate it into russian'
    )


def translator(update, context):
    answer = translate(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=answer)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

translate_handler = MessageHandler(Filters.text, translator)
dispatcher.add_handler(translate_handler)

updater.start_polling()


