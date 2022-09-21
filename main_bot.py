from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other


async def on_startup(_):  # Отображает статус бота (отладчик в консоли запуска)
    print('Бот вышел в онлайн!')


client.register_handlers_client(dp)  # Модуль обработки клиентской части
admin.register_handlers_admin(dp)  # Модуль обработки Админской части
other.register_handlers_other(dp)  # Модуль обработки мата, содержит пустой хендлер, должен стоять последним


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
