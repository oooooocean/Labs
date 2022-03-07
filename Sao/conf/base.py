from collections import namedtuple

SERVER_HOST = 'http://127.0.0.1:8000'

ErrorCode = namedtuple('ErrorCode', ['msg', 'code'])

ERROR_CODE_0 = ErrorCode('ok', 0)
ERROR_CODE_1001 = ErrorCode('非法参数', 1001)


