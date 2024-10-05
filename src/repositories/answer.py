from sqlalchemy.ext.asyncio import async_sessionmaker

from src.models import Answer


class AnswerRepository:

    @staticmethod
    async def create(sessions: async_sessionmaker, user_id: int, answers: dict, score: int) -> Answer:
        answer = Answer(user_id=user_id, answers=answers, score=score)
        async with sessions() as session:
            session.add(answer)
            await session.commit()
        return answer
