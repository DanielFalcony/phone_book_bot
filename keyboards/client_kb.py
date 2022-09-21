from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Кнопки навигации в боте
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/показать_весь_список_контактов')
b3 = KeyboardButton('/добавить_контакт')
b4 = KeyboardButton('/удалить_контакт')
b5 = KeyboardButton('/редактировать_контакт')
b6 = KeyboardButton('/найти_контакт')
b7 = KeyboardButton('/импорт_контактов')
b8 = KeyboardButton('/экспорт_контактов')


# Создание класса замещения клавиатуры пользователя на кнопки навигации в боте
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем кнопки в клавиатуру
kb_client.add(b1).add(b2).add(b3).add(b4).add(b5).add(b6).add(b7).add(b8)
