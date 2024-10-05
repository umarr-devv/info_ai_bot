from aiogram import types, Router, F, Bot
from aiogram.utils.chat_action import ChatActionSender
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.repositories import ContentRepository, PromptRepository
from src.service.ai_client import AiApiClient
from src.service.rag import extract_text

router = Router()


@router.message(F.content_type == types.ContentType.TEXT)
async def on_chat(message: types.Message,
                  bot: Bot,
                  ai_client: AiApiClient,
                  sessions: async_sessionmaker):
    async with ChatActionSender.typing(chat_id=message.chat.id, bot=bot):
        query = message.text
        system_prompt = await PromptRepository.by_name(sessions, name='system-prompt')
        contents = await ContentRepository.all_content(sessions)
        extract_content = extract_text(contents, query, 5)

        prompt = system_prompt.content.format(''.join(extract_content),
                                              message.from_user.first_name)

        text = await ai_client.completion(query=message.text, system_prompt=prompt)
        await message.answer(text)
