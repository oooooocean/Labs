import conf.db
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship
from models.base_model import ModelMixin


class Album(conf.db.BaseDB, ModelMixin):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    create_time = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='albums')

    photos = relationship('Photo', back_populates='album', uselist=True)


class Photo(conf.db.BaseDB, ModelMixin):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    create_time = Column(Integer, nullable=False)

    album_id = Column(Integer, ForeignKey('album.id'))
    album = relationship('Album', back_populates='photos')
