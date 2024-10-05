import asyncio
import random

from aiogram import types, Router, Bot
from aiogram.filters import CommandObject, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.chat_action import ChatActionSender
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.service.ai_client import AiApiClient
from src.repositories import AnswerRepository
from src.repositories import ContentRepository, PromptRepository

router = Router()


class QuestionState(StatesGroup):
    question = State()


async def create_question(sessions: async_sessionmaker, ai_client: AiApiClient) -> list[str]:
    prompt = await PromptRepository.by_name(sessions, 'question-prompt')
    content = await ContentRepository.random(sessions)
    question = await ai_client.completion(query='',
                                          system_prompt=prompt.content.format(content),
                                          temperature=0.9)
    return question.split('|')


async def create_message(sessions: async_sessionmaker,
                         ai_client: AiApiClient) -> tuple[str, types.InlineKeyboardMarkup]:
    question, answer, *wrong_answers = await create_question(sessions, ai_client)

    buttons = [types.InlineKeyboardButton(text=value, callback_data='false') for value in wrong_answers]
    buttons.append(types.InlineKeyboardButton(text=answer + '!', callback_data='true'))
    random.shuffle(buttons)

    text = f'<b>❓ Вопрос:</b>\n\n {question}'
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [button] for button in buttons
        ]
    )
    return text, keyboard


@router.message(Command(commands=['test']))
async def on_test(message: types.Message,
                  command: CommandObject,
                  ai_client: AiApiClient,
                  sessions: async_sessionmaker,
                  state: FSMContext,
                  bot: Bot):
    text = f'❕ Сейчас мы зададим несколько <b>вопросов</b>, чтобы понять насколько хорошо вы усвоили материал'
    async with ChatActionSender.typing(chat_id=message.chat.id, bot=bot):
        await message.answer(text=text)
        await asyncio.sleep(0.25)

        text, keyboard = await create_message(sessions, ai_client)
        await message.answer(text=text, reply_markup=keyboard)

        await state.set_state(QuestionState.question)
        await state.set_data({'answers': [], 'index': 5, 'score': 0})


@router.callback_query(StateFilter(QuestionState.question))
async def on_question(callback: types.CallbackQuery,
                      ai_client: AiApiClient,
                      sessions: async_sessionmaker,
                      state: FSMContext,
                      bot: Bot):
    await callback.answer()

    data = await state.get_data()

    data['score'] += 1 if callback.data == 'true' else 0
    data['index'] -= 1
    data['answers'].append({'question': callback.message.text,
                            "answer": True if callback.data == 'true' else False})
    await state.set_data(data)

    if data['index'] == 0:
        text = f'☑️ Тест окончен. <b>Вы</b> ответили' \
               f' на <code>{data["score"]}/5</code> вопросов правильно'
        await callback.message.edit_text(text=text, reply_markup=None)
        await AnswerRepository.create(sessions,
                                      user_id=callback.from_user.id,
                                      answers=data['answers'],
                                      score=data['score'])
        await state.clear()
        return

    async with ChatActionSender.typing(chat_id=callback.message.chat.id, bot=bot):
        text, keyboard = await create_message(sessions, ai_client)
        await callback.message.edit_text(text=text, reply_markup=keyboard)
