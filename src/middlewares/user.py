from aiogram import types
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from src.repositories import UserRepository


class UserMiddleware(BaseMiddleware):

    async def __call__(self,
                       handler,
                       event: types.Message | types.CallbackQuery,
                       data: dict) -> any:
        sessions = data.get('sessions')
        user_id = event.from_user.id

        user = await UserRepository.by_user_id(sessions, user_id)

        if not user:
            user = await UserRepository.create(sessions, user_id)

        data['user'] = user

        return await handler(event, data)
