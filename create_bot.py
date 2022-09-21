from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

# bot = Bot(token=os.getenv('TOKEN'))  # Принимает токен из *.bat
bot = Bot(token='5601243555:AAH93TKtvFElJjFJwtzsW0PfeTONsAYPn7s')  # Прямая передача токена
dp = Dispatcher(bot)
