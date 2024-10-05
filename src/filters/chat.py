from aiogram import types
from aiogram.filters import BaseFilter

from src.config import Config


class AdminFilter(BaseFilter):

    async def __call__(self, get: types.Message | types.CallbackQuery, config: Config):
        return get.from_user.id == config.bot.admin_id
    