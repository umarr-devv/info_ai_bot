from aiogram import types, Router
from aiogram.filters import CommandStart, CommandObject

router = Router()


@router.message(CommandStart())
async def on_start(message: types.Message, command: CommandObject):
    text = f'Привет, {message.from_user.first_name}!\n\n' \
           '👋 Я бот, который расскажет тебе о <b>Хакатоне</b> и бирже <b>Latoken!</b>\n' \
           ' 🚀 Узнаешь, как погрузиться в мир инноваций, создать крутые проекты' \
           ' и получить возможность сотрудничества с одной из ведущих криптобирж.' \
           ' Готов к погружению в захватывающий мир технологий и финансов? Поехали! 💡 '
    await message.answer(text=text)
