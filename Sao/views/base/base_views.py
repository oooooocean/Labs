from tornado.web import RequestHandler
from models.user_model import User
import conf.base
import json
from common.jwt_utils import JWTUtils
import time
from conf.base import ERROR_CODE_0
import jwt


class BaseHandler(RequestHandler):
    def http_response(self, error: conf.base.ErrorCode, data=None):
        self.finish(json.dumps({'msg': error.msg, 'code': error.code, 'data': data}))


class AuthBaseHandler(BaseHandler):

    def prepare(self):
        try:
            jwt_string = self.request.headers['Authorization']
        except KeyError:
            self.http_response(conf.base.ERROR_CODE_1000)
            return

        try:
            jwtPayload = JWTUtils.parse(jwt_string)
        except jwt.exceptions.ExpiredSignatureError:
            self.http_response(conf.base.ERROR_CODE_1003)
            return

        if not jwtPayload.uid or not jwtPayload.exp:
            self.http_response(conf.base.ERROR_CODE_1000)
            return

        # 检查 token 是否过期
        if jwtPayload.exp <= time.time():
            self.http_response(conf.base.ERROR_CODE_1003)
            return

        # 检查用户
        self.current_user = User.query.filter(User.id == jwtPayload.uid).first()
        if not self.current_user:
            self.http_response(conf.base.ERROR_CODE_1004)
            return
