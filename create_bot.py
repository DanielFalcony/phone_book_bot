from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

# bot = Bot(token=os.getenv('TOKEN'))  # Принимает токен из *.bat
bot = Bot(token='5601243555:AAH93TKtvFElJjFJwtzsW0PfeTONsAYPn7s')  # Прямая передача токена
dp = Dispatcher(bot, storage=storage)
