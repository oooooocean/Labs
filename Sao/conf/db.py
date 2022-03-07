from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from importlib import import_module

db_engine = create_engine('mysql+mysqldb://root:bei1202jing@127.0.0.1:3306/sao',
                          encoding='utf8',
                          echo=False,
                          future=True)

# registry().generate_base()
BaseDB = declarative_base(db_engine)

sessions = scoped_session(sessionmaker(bind=db_engine, autocommit=False, autoflush=True, expire_on_commit=False))


def init_db():
    import_module('models')  # 利用导入时, 获取数据库实体类信息
    BaseDB.metadata.create_all()  # 初始化数据库