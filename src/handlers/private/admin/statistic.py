from aiogram import types, Router, Bot
from aiogram.filters.command import Command, CommandObject
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.repositories import UserRepository

router = Router()


@router.message(Command(commands=['user']))
async def on_user_info(message: types.Message,
                       command: CommandObject,
                       sessions: async_sessionmaker,
                       bot: Bot):
    user_id = command.args
    if not user_id:
        text = '❌ Введите <b>ID</b> пользователя после команды <code>/user</code>'
        await message.answer(text=text)
        return

    if not user_id.isdigit():
        text = '❌ Значние после команды <code>/user</code> должен быть числовым'
        await message.answer(text=text)
        return

    user_id = int(user_id)
    user = await UserRepository.by_user_id(sessions, user_id)

    if not user:
        text = f'❓ Пользователь с <b>ID</b> <code>{user_id}</code> не найден'
        await message.answer(text=text)
        return

    chat = await bot.get_chat(chat_id=user_id)

    text = f'👤 Пользователь c <b>ID</b> {user.user_id}\n\n' \
           f'<b>ФИО</b>: <code>{chat.full_name}</code>\n' \
           f'<b>ID в базе</b>: <code>{user.id}</code>\n' \
           f'<b>Дата регистрации</b>: <code>{user.created_on}</code>'
    await message.answer(text=text)
