from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ChatType
from telethon import TelegramClient

API_TOKEN = ""  # Ваш токен бота
API_ID = 0  # Ваш API_ID бота
API_HASH = ""  # Ваш API_ID хэш

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


# * Команда /help
@dp.message_handler(commands='help', chat_type=ChatType.SUPERGROUP)
async def help_command(message: types.Message):
    help_text = ('Доступные команды:\n'
                 '/help - показать доступные команды\n'
                 '/all - тегнуть всех пользователей\n')
    await message.reply(help_text)


# * Команда /all
@dp.message_handler(commands='all', chat_type=ChatType.SUPERGROUP)
async def all_users(message: types.Message):
    try:
        client = TelegramClient('bot', API_ID, API_HASH)
        async with client:
            objects_members, all_members = [], []
            objects_members = await client.get_participants(message["chat"]["id"], aggressive=True)
            for member in objects_members:
                if member.id != 6374906339:
                    all_members.append(member.id)
    except:
        await message.reply("Произошла ошибка!")

    link_users = list()

    for i in all_members:
        user = await bot.get_chat_member(chat_id=message.chat.id, user_id=i)
        link_users.append(
            f'<a href="tg://user?id={i}">{user.user.full_name}</a>')
    await message.reply(f"Важная информация!\n\n{', '.join(link_users)}", parse_mode="HTML")


# * Вывод кода в тг
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
