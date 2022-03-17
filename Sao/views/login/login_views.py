import logging
from models.user_model import User
from datetime import datetime
from views.base.base_views import BaseHandler
import common.jwt_utils
from service.utils import check_code
from common.exception import (
    ERROR_CODE_0,
    ERROR_CODE_1001,
    ERROR_CODE_1002
)


class LoginHandler(BaseHandler):
    def post(self):
        """
        登录
        """
        try:
            phone = self.json_args['phone']
            code = self.json_args['code']
        except KeyError:
            raise ERROR_CODE_1001
        else:
            if not check_code(code):
                raise ERROR_CODE_1002
            ex_user = User.query.filter_by(phone=phone).first()
            if not ex_user:
                logging.info('LoginHandle/post: 插入新用户 %r' % (phone,))
                ex_user = User(phone=phone, create_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                ex_user.save()
            user_json = ex_user.to_json()
            token = common.jwt_utils.JWTUtils.create(ex_user.id)
            self.http_response(ERROR_CODE_0, {'user': user_json, 'token': token})
