from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship, Query
from models.base_model import ModelMixin
from conf.db import BaseDB


class User(BaseDB, ModelMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(11), nullable=False)
    create_time = Column(DateTime, nullable=True)

    info = relationship('UserInfo', back_populates='user', uselist=False)


class UserInfo(BaseDB, ModelMixin):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates="info")
