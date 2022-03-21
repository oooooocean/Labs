from tornado.web import RequestHandler
from models.user_model import User
import json
from common.jwt_utils import JWTUtils
from common.exception import (
    ERROR_CODE_0,
    ERROR_CODE_1000,
    ERROR_CODE_1003,
    SaoException
)
import jwt
from tornado.escape import json_decode


class BaseHandler(RequestHandler):
    def prepare(self):
        if self.request.headers.get('Content-Type', '').startswith('application/json'):
            self.json_args = json_decode(self.request.body)
        else:
            self.json_args = None

    def http_response(self, error: SaoException, data=None):
        """
        响应
        :param error: 错误码
        :param data: 数据体
        :return:
        """
        self.set_status(error.getHttpStatus())
        self.finish(json.dumps({'msg': error.msg, 'code': error.code, 'data': data}))

    def success(self, data):
        self.finish(json.dumps({'msg': ERROR_CODE_0.msg, 'code': ERROR_CODE_0.code, 'data': data}))

    def write_error(self, status_code: int, **kwargs) -> None:
        exc_info = kwargs.get('exc_info', None)
        if exc_info[0] is SaoException:
            self.http_response(exc_info[1])
            return
        super().write_error(status_code, **kwargs)


class AuthBaseHandler(BaseHandler):

    def prepare(self):
        try:
            jwt_string = self.request.headers['Authorization']
            jwtPayload = JWTUtils.parse(jwt_string)
            self.current_user = User.query.filter(User.id == jwtPayload.uid).first()
            assert self.current_user
        except jwt.exceptions.ExpiredSignatureError:
            raise ERROR_CODE_1003
        except Exception:
            raise ERROR_CODE_1000
        else:
            super(AuthBaseHandler, self).prepare()
