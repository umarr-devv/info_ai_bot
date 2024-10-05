import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import Config
from src.handlers import router
from src.service.database import DataBase
from src.utils.commands import set_commands
from src.utils.logs import set_logging
from src.models import Base

CONFIG_FILE = 'local-config.yml'

config = Config.create(config_file=CONFIG_FILE)
dp = Dispatcher(storage=MemoryStorage())
database = DataBase(config)
bot = Bot(token=config.bot.token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main():
    set_logging(config)
    await set_commands(bot)

    dp.include_router(router)

    try:
        await dp.start_polling(bot, sessions=database.sessions, config=config)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())
