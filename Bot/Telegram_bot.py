import telegram
from dotenv import load_dotenv
import os

from telegram.ext import Updater

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telegram.Bot(token=TELEGRAM_TOKEN)
updater = Updater(token='TOKEN', use_context=True)
