from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Кнопки навигации в боте
b1 = KeyboardButton('/показать_весь_список_контактов')
b2 = KeyboardButton('/добавить_контакт')
b3 = KeyboardButton('/удалить_контакт')
b4 = KeyboardButton('/редактировать_контакт')
b5 = KeyboardButton('/найти_контакт')
b6 = KeyboardButton('/импорт_контактов')
b7 = KeyboardButton('/экспорт_контактов')
b8 = KeyboardButton('/help')

# Создание класса замещения клавиатуры пользователя на кнопки навигации в боте
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем кнопки в клавиатуру
kb_client.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8)
