from collections import namedtuple

SERVER_HOST = 'http://127.0.0.1:8000'

ErrorCode = namedtuple('ErrorCode', ['msg', 'code'])

ERROR_CODE_0 = ErrorCode('ok', 0)
ERROR_CODE_1000 = ErrorCode('Authorization 缺失', 1000)
ERROR_CODE_1001 = ErrorCode('非法参数', 1001)
ERROR_CODE_1002 = ErrorCode('验证码错误', 1002)
ERROR_CODE_1003 = ErrorCode('登录过期', 1003)
ERROR_CODE_1004 = ErrorCode('非法用户', 1004)



