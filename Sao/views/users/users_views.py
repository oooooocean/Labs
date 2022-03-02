import conf.base
import tornado.web
from tornado.escape import json_decode
from common.commons import http_response


class LoginHandle(tornado.web.RequestHandler):
    def post(self):
        try:
            print(self.request.body)
            args = json_decode(self.request.body)
            phone = args['phone']
            code = args['code']
        except Exception as e:
            http_response(self, conf.base.ERROR_CODE_1001, str(e))
            return

        http_response(self, conf.base.ERROR_CODE_0)
