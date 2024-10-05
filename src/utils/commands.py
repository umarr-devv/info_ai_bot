from aiogram import types, Bot


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            types.BotCommand(
                command='start', description='Запустить бота'
            ),
            types.BotCommand(
                command='/test', description='Запустить тест'
            )
        ],
        scope=types.BotCommandScopeAllPrivateChats()
    )
