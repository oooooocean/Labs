from service.utils import save_images
from models.user_model import UserInfo, User
from views.base.base_views import AuthBaseHandler
from conf.db import sessions
from common.exception import (
    ERROR_CODE_0,
    ERROR_CODE_1006
)


class UserHandler(AuthBaseHandler):

    def prepare(self):
        uid = self.path_args[0]
        self.user = sessions.get(User, uid)
        assert self.user and not self.user.deleted, '用户不存在, uid: %r' % uid
        super(AuthBaseHandler, self).prepare()

    def get(self, _):
        """
        获取用户的基本信息
        :return:
        """
        return self.http_response(ERROR_CODE_0, self.user.to_json())

    def post(self, _):
        """
        修改用户信息
        :return:
        """

        user_info: UserInfo = self.user.info or UserInfo()
        user_info.nickname = self.get_body_argument('nickname', user_info.nickname)
        user_info.gender = self.get_body_argument('gender', user_info.gender)
        image_mates = self.request.files.get('image', None)
        if image_mates:
            user_info.avatar = save_images(image_mates)[0]

        self.user.info = user_info
        self.user.save()

        json = self.user.to_json()
        json['info'] = self.user.info.to_json()
        self.http_response(ERROR_CODE_0, json)
