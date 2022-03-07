from conf.db import sessions
from sqlalchemy.orm import Query


class ModelMixin:
    query: Query = sessions.query_property()