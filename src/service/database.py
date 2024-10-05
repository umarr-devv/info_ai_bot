from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.config import Config

URL_TEMPLATE = 'postgresql+asyncpg://{}:{}@{}/{}'


class Base(DeclarativeBase):
    __abstract__ = True


class DataBase:

    def __init__(self, config: Config):
        self.url = URL_TEMPLATE.format(config.db.user, config.db.password,
                                       config.db.host, config.db.database)
        self.engine = create_async_engine(
            url=self.url
        )
        self.sessions = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )
