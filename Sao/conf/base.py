from collections import namedtuple

ErrorCode = namedtuple('ErrorCode', ['msg', 'code'])

ERROR_CODE_0 = ErrorCode('ok', 0)
ERROR_CODE_1001 = ErrorCode('非法参数', 1001)
