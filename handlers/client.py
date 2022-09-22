from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в Телефонный справочник!',
                               reply_markup=kb_client)  # обработка команд /start
        await message.delete()
    except BaseException:  # Нужен тест на захват исключения
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Phone_book_PY3052_bot') # Вывод ответа в чат бота


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Справка')


# @dp.message_handler(commands=['показать_весь_список_контактов'])
async def list_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Список контактов')


# @dp.message_handler(commands=['добавить_контакт'])
async def add_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добавить')


# @dp.message_handler(commands=['удалить_контакт'])
async def del_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Удалить')


# @dp.message_handler(commands=['редактировать_контакт'])
async def rename_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Редактировать')


# @dp.message_handler(commands=['найти_контакт'])
async def search_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Найти')


# @dp.message_handler(commands=['импорт_контактов'])
async def import_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Импорт')


# @dp.message_handler(commands=['экспорт_контактов'])
async def export_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Экспорт')


# Создаем диспетчер функций
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, text=['Справка'])
    dp.register_message_handler(list_contact, text=['Показать весь список контактов'])
    dp.register_message_handler(add_contact, text=['Добавить контакт'])
    dp.register_message_handler(del_contact, text=['Удалить контакт'])
    dp.register_message_handler(rename_contact, text=['Редактировать контакт'])
    dp.register_message_handler(search_contact, text=['Найти контакт'])
    dp.register_message_handler(import_contact, text=['Импорт контактов'])
    dp.register_message_handler(export_contact, text=['Экспорт контактов'])
