from loguru import logger
from tornado.httputil import HTTPServerRequest


def config_log():
    """
    日志配置
    Once the file is too old, it's rotated
    :return:
    """
    logger.add('log/log_{time}.log', rotation='3 days', level='ERROR', backtrace=False, retention=5)


def log_request_error(uid: str, request: HTTPServerRequest):
    request_info = 'uid: %r, requst: %r, query: %r, body %r' % (uid, request, request.query, request.body)
    logger.exception(request_info)
