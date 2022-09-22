from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Кнопки навигации в боте
b1 = KeyboardButton('Показать весь список контактов')
b2 = KeyboardButton('Добавить контакт')
b3 = KeyboardButton('Удалить контакт')
b4 = KeyboardButton('Редактировать контакт')
b5 = KeyboardButton('Найти контакт')
b6 = KeyboardButton('Импорт контактов')
b7 = KeyboardButton('Экспорт контактов')
b8 = KeyboardButton('Справка')
b9 = KeyboardButton('Поделиться номером', request_contact=True)



# Создание класса замещения клавиатуры пользователя на кнопки навигации в боте
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

# Добавляем кнопки в клавиатуру
kb_client.add(b1).add(b2).insert(b3).add(b4).insert(b5).add(b6).insert(b7).add(b8).add(b9)
