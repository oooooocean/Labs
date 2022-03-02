import json
from tornado.web import RequestHandler
from conf.base import ErrorCode


def http_response(self: RequestHandler, error: ErrorCode, data=None):
    self.write(json.dumps({'msg': error.msg, 'code': error.code, 'data': data}))
