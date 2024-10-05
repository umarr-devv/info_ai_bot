from datetime import datetime

from sqlalchemy import (Column, Date, Integer, ForeignKey, JSON, Float)

from src.service.database import Base


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey('users.user_id'), nullable=False)
    answers = Column(JSON, nullable=False)
    score = Column(Float, default=0, nullable=False)
    created_on = Column(Date, default=datetime.now)
    update_on = Column(Date, default=datetime.now, onupdate=datetime.now)
