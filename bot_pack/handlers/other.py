from aiogram import types, Dispatcher
import json, string
from create_bot import dp


@dp.message_handler()
async def cenzor_send(message: types.Message):  # Реализован фильтр матов, с учетом подмены букв символами
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(cenzor_send)
