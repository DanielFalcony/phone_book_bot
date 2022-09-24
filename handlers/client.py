from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
# from Commands.Import import import_any_file as input_file


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в Телефонный справочник!',
                               reply_markup=kb_client)  # обработка команд /start
        await message.delete()
    except BaseException:  # Нужен тест на захват исключения
        await message.reply(
            'Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Phone_book_PY3052_bot')  # Вывод ответа в чат бота


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Это справка по данному боту')


# @dp.message_handler(commands=['показать_весь_список_контактов'])
async def list_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь будет список контактов')


# @dp.message_handler(commands=['добавить_контакт'])
async def add_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь будет поиск контактов')


# @dp.message_handler(commands=['удалить_контакт'])
async def del_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь можно удалить контак')


# @dp.message_handler(commands=['редактировать_контакт'])
async def rename_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь можно отредактировать контакт')


# @dp.message_handler(commands=['найти_контакт'])
async def search_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь можно найти контакт')


@dp.message_handler(commands=['импорт_контактов'])
async def import_contact(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = (message.document.file_name)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        await bot.reply_to(message, "Файл сохранен.")


# @dp.message_handler(commands=['экспорт_контактов'])
async def export_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь можно экспортировать контакт')


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
