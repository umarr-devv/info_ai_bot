from aiogram import Router

from src.handlers.private.user.start import router as start_router
from src.handlers.private.user.chat import router as chat_router
from src.handlers.private.user.test import router as test_router


router = Router()

router.include_router(start_router)
router.include_router(test_router)
router.include_router(chat_router)
