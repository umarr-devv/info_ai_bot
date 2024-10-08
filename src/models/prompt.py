from datetime import datetime

from sqlalchemy import (Column, Date, Integer, String, Text)

from src.service.database import Base


class Prompt(Base):
    __tablename__ = 'prompts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    created_on = Column(Date, default=datetime.now)
    update_on = Column(Date, default=datetime.now, onupdate=datetime.now)
