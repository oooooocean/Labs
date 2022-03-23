from models.user_model import User
from views.base.base_views import BaseHandler
import common.jwt_utils
from service.utils import check_code
from loguru import logger
from common.exception import ERROR_CODE_1001
from service.password import validate_password


class LoginHandler(BaseHandler):
    def post(self):
        """
        登录
        """
        phone = self.json_args.get('phone', None)
        password = self.json_args.get('password', None)
        code = self.json_args.get('code', None)

        assert phone, '手机号不能为空'

        if password:
            self._login_with_password(phone, password)
        elif code:
            self._login_with_code(phone, code)
        else:
            raise ERROR_CODE_1001

    def _login_with_password(self, phone, password):
        """
        密码登录
        :param phone:
        :param password:
        :return:
        """
        user = User.query.filter_by(phone=phone).first()
        assert user, '用户不存在'
        assert user.password, '用户密码不存在, 请先设置密码'
        assert validate_password(user.password, password), '密码错误'
        self._login_success(user)

    def _login_with_code(self, phone, code):
        """
        验证码登录, 如果用户不存在, 则自动注册
        :param phone:
        :param code:
        :return:
        """
        assert check_code(code), '验证码错误'
        user = User.query.filter_by(phone=phone).first() or self._add_new_user(phone)
        self._login_success(user)

    def _login_success(self, user):
        """
        登录成功
        :param user:
        :return: 用户信息和token
        """
        user_json = user.to_json()
        token = common.jwt_utils.JWTUtils.create(user.id)
        self.success({'user': user_json, 'token': token})

    def _add_new_user(self, phone):
        """
        添加新用户
        :param phone:
        :return:
        """
        logger.info('LoginHandle/post: 插入新用户 %r' % (phone,))
        ex_user = User(phone=phone)
        ex_user.save()
        return ex_user
