from conf.db import sessions, BaseDB
from sqlalchemy.orm import Query
import datetime
from common.utils import camel_case


class ModelMixin:
    query: Query = sessions.query_property()

    def to_json(self):
        json_dict = {}
        for column in self.__table__.columns:
            name = column.name
            key_name = camel_case(name)
            value = getattr(self, name)
            if isinstance(value, datetime.datetime):
                json_dict[key_name] = int(value.timestamp())
            elif isinstance(value.__class__, BaseDB):
                json_dict[key_name] = value.to_json()
            else:
                json_dict[key_name] = value
        return json_dict
