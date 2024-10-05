from aiogram import Router

from src.handlers.private.user.start import router as start_router

router = Router()

router.include_router(start_router)
