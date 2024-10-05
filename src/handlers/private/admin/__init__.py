from aiogram import Router

from src.filters.chat import AdminFilter
from src.handlers.private.admin.statistic import router as statistic_router

router = Router()

router.include_router(statistic_router)
router.message.filter(AdminFilter())
router.callback_query.filter(AdminFilter())
