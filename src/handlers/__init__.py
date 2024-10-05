from aiogram import Router

from src.handlers.channel import router as channel_router
from src.handlers.group import router as group_router
from src.handlers.private import router as private_router

router = Router()

router.include_router(private_router)
router.include_router(group_router)
router.include_router(channel_router)
