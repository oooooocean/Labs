from service.utils import save_images
from models.user_model import UserInfo, User
from views.base.base_views import AuthBaseHandler
from common.exception import (
    ERROR_CODE_0,
)


class UserHandler(AuthBaseHandler):

    def get(self):
        """
        获取用户的基本信息
        :return:
        """
        user = self.current_user
        uid = self.request.arguments.get('uid', None)
        if uid:
            user = User.query.filter_by(id=uid).first()
        return self.http_response(ERROR_CODE_0, user.to_json())

    def post(self):
        """
        修改用户信息
        :return:
        """
        user_info: UserInfo = self.current_user.info
        if not user_info:
            user_info = UserInfo()
        user_info.nickname = self.get_body_argument('nickname', user_info.nickname)
        user_info.gender = self.get_body_argument('gender', user_info.gender)
        image_mates = self.request.files.get('image', None)
        if image_mates:
            user_info.avatar = save_images(image_mates)[0]

        self.current_user.info = user_info
        self.current_user.save()
        json = self.current_user.to_json()
        json['info'] = self.current_user.info.to_json()
        self.http_response(ERROR_CODE_0, json)
