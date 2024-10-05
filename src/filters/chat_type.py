from aiogram import types
from aiogram.enums.chat_type import ChatType
from aiogram.filters import BaseFilter


class ChatTypeFilter(BaseFilter):
    chat_types: list[str] = []

    async def __call__(self, message: types.Message | types.CallbackQuery) -> bool:
        if isinstance(message, types.CallbackQuery):
            message = message.message
        return message.chat.type in self.chat_types


class PrivateTypeFilter(ChatTypeFilter):
    chat_types: list[str] = [ChatType.PRIVATE]


class GroupTypeFilter(ChatTypeFilter):
    chat_types: list[str] = [ChatType.GROUP, ChatType.SUPERGROUP]


class ChannelTypeFilter(ChatTypeFilter):
    chat_types: list[str] = [ChatType.CHANNEL]
