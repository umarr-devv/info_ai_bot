from aiogram import Router

from src.filters.chat_type import ChannelTypeFilter

router = Router()

router.message.filter(ChannelTypeFilter())
router.callback_query.filter(ChannelTypeFilter())
