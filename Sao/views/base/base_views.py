from tornado.web import RequestHandler
from models.models import User
from conf.base import ErrorCode
import json


class BaseHandle(RequestHandler):
    def http_response(self, error: ErrorCode, data=None):
        self.write(json.dumps({'msg': error.msg, 'code': error.code, 'data': data}))

    def get_current_user(self):
        token = self.request.headers['token']
        if token:
            return User.query.filter(User.token == token).first()
        return None
