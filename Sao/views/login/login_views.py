import conf.base
import tornado.web
from tornado.escape import json_decode
from common.commons import http_response
import logging
from conf.db import sessions
from models.models import User
from datetime import datetime


class LoginHandle(tornado.web.RequestHandler):

    def get(self):
        self.render('web/index.html')
        return

    def post(self):
        try:
            args = json_decode(self.request.body)
            phone = args['phone']
            code = args['code']
        except Exception as e:
            logging.info('LoginHandle/post: %r' % (str(e),))
            http_response(self, conf.base.ERROR_CODE_1001)
            return

        ex_user = User.query.filter(User.phone == phone).first()
        if ex_user:
            http_response(self, conf.base.ERROR_CODE_0)
            sessions.close()
            return
        else:
            logging.info('LoginHandle/post: 插入新用户 %r' % (phone,))
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_user = User(phone=phone, create_time=create_time)
            sessions.add(new_user)
            sessions.commit()
            sessions.close()
            http_response(self, conf.base.ERROR_CODE_0)
