from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text


class FSMAdmin(StatesGroup):
    name = State()
    phone = State()


# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.name.set()
    await message.reply('Укажи ФИО:')


# Ловим первый ответ и пишем в словарь (ФИО)
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь введи номер телефона:')


# Ловим второй ответ и пишем в словарь (Телефон)
# @dp.message_handler(state=FSMAdmin.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь введи номер телефона:')

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


# Выход из машины состояний (отмена ввода)
# @dp.message_handler(state='*', commands='Отмена')
# @dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('ОК')


# Регистрируем хендлеры
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_phone, state=FSMAdmin.phone)
    dp.register_message_handler(cancel_handler, state='*', commands='Отмена')
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state='*')
