import conf.base
import tornado.web
from tornado.escape import json_decode, json_encode
import logging
from conf.db import sessions
from models.user_model import User
from datetime import datetime
from views.base.base_views import BaseHandler
import common.jwt_utils


class LoginHandler(BaseHandler):

    def get(self):
        return 'hello, world'

    def post(self):
        """
        登录
        """
        try:
            # 解析 application-json
            args = json_decode(self.request.body)
            phone = args['phone']
            code = args['code']
        except Exception as e:
            logging.info('LoginHandle/post: %r' % (str(e),))
            self.http_response(conf.base.ERROR_CODE_1001)
            return

        if not self.check_code(code):
            logging.error('验证码错误: %r' % code)
            self.http_response(conf.base.ERROR_CODE_1002)
            return

        # ex_user = User.query.filter(User.phone == phone).first()
        ex_user = User.query.filter_by(phone=phone).first()

        if not ex_user:
            logging.info('LoginHandle/post: 插入新用户 %r' % (phone,))
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ex_user = User(phone=phone, create_time=create_time)
            sessions.add(ex_user)
            sessions.commit()
            sessions.close()

        user_json = ex_user.to_json()
        token = common.jwt_utils.JWTUtils.create(ex_user.id)
        self.http_response(conf.base.ERROR_CODE_0, {'user': user_json, 'token': token})

    def check_code(self, code):
        """
        检查验证码
        """
        return code == '123456'
