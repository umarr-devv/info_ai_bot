from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.baked import Result

from src.models import Content


class ContentRepository:

    @staticmethod
    async def by_name(sessions: async_sessionmaker, name: str) -> Content:
        statement = select(Content).where(Content.name == name)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalar()

    @staticmethod
    async def all(sessions: async_sessionmaker) -> list[Content]:
        statement = select(Content).order_by(Content.id)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalars().all()

    async def all_content(sessions: async_sessionmaker) -> list[str]:
        statement = select(Content.content).order_by(Content.id)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalars().all()
