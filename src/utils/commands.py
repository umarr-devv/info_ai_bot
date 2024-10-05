from aiogram import types, Bot


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            types.BotCommand(
                command='start', description='Запустить бота'
            ),
            types.BotCommand(
                command='help', description='Помощь'
            )
        ],
        scope=types.BotCommandScopeAllPrivateChats()
    )
