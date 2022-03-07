import conf.base
import tornado.web
from tornado.escape import json_decode, json_encode
import logging
from conf.db import sessions
from models.models import User
from datetime import datetime
from views.base.base_views import BaseHandle


class UserHandle(BaseHandle):

    def get(self):
        if self.current_user is None:
            return self.http_response(conf.base.ERROR_CODE_1001)
        return self.http_response(conf.base.ERROR_CODE_0, json_encode(self.current_user))

