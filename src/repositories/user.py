from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.baked import Result

from src.models import User


class UserRepository:

    @staticmethod
    async def create(sessions: async_sessionmaker, user_id: int) -> User:
        user = User(user_id=user_id)
        async with sessions() as session:
            session.add(user)
            await session.commit()
        return user

    @staticmethod
    async def by_user_id(sessions: async_sessionmaker, user_id: int) -> User:
        statement = select(User).where(User.user_id == user_id)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalar()

    @staticmethod
    async def all(sessions: async_sessionmaker) -> list[User]:
        statement = select(User).order_by(User.id)
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalars().all()

    @staticmethod
    async def count(sessions: async_sessionmaker) -> int:
        statement = select(func.count(User.id))
        async with sessions() as session:
            result: Result = await session.execute(statement)
        return result.scalar()
