import os
import random

import telegram
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from translater.main import lang_detect, main as translate

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telegram.Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    """Description command"""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='I am an interpreter bot, send me a text '
             'and i will translate it into russian. '
             'input /about for list of commands '
             'text without command will give you some random fun :wink:'
    )


def about(update, context):
    """Available commands list"""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='/detect will help you to find what language is '
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='/translate will help you to translate phrase '
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='syntax is  /command YOUR TEXT'
    )


def detect(update, context):
    """Detecting language of text"""
    sentence = ' '.join(context.args)
    answer = lang_detect(sentence)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=answer)


def translator(update, context):
    """Translating text"""
    sentence = ' '.join(context.args)
    answer = translate(sentence)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=answer)


def fun(update, context):
    """Just some fun"""
    sequence = ('rev', 'shout', 'only', 'miss')
    choice = random.choice(sequence)
    if choice == 'rev':
        answer = update.message.text[::-1]
    elif choice == 'only':
        answer = 'You are the chosen one'
    elif choice == 'shout':
        answer = update.message.text.upper()
    elif choice == 'miss':
        answer = 'Missed! Try again!'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=answer
    )


def unknown(update, context):
    """Unknown commands"""
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Unknown command, pls check and try again!')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

about_handler = CommandHandler('about', about)
dispatcher.add_handler(about_handler)

translate_handler = CommandHandler('translate', translator)
dispatcher.add_handler(translate_handler)

detect_handler = CommandHandler('detect', detect)
dispatcher.add_handler(detect_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

fun_handler = MessageHandler(Filters.text, fun)
dispatcher.add_handler(fun_handler)

# updater.start_polling(poll_interval=15)
updater.start_polling()
