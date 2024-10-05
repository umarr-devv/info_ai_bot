from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.baked import Result

from src.models import Prompt


class PromptRepository:

    @staticmethod
    async def by_name(sessions: async_sessionmaker, name: str) -> Prompt:
        statement = select(Prompt).where(Prompt.name == name)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalar()

    @staticmethod
    async def all(sessions: async_sessionmaker) -> list[Prompt]:
        statement = select(Prompt).order_by(Prompt.id)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalars().all()

    async def all_content(sessions: async_sessionmaker) -> list[str]:
        statement = select(Prompt.content).order_by(Prompt.id)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalars().all()
