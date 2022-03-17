class SaoException(Exception):
    def __init__(self, code, msg, detail=None):
        self.code = code
        self.msg = msg
        self.detail = detail


ERROR_CODE_0 = SaoException('ok', 0)
ERROR_CODE_1000 = SaoException('Authorization 缺失', 1000)
ERROR_CODE_1001 = SaoException('非法参数', 1001)
ERROR_CODE_1002 = SaoException('验证码错误', 1002)
ERROR_CODE_1003 = SaoException('登录过期', 1003)
ERROR_CODE_1004 = SaoException('非法用户', 1004)
ERROR_CODE_1005 = SaoException('数据重复', 1005)
