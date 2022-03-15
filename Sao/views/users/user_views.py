from tornado.escape import json_decode, json_encode

import conf.base
from common.utils import save_images
from conf.db import sessions
from models.gender import Gender
from models.user_model import UserInfo, User
from views.base.base_views import AuthBaseHandler
from sqlalchemy.orm import Query


class UserHandler(AuthBaseHandler):

    def get(self):
        user = self.current_user
        uid = self.request.arguments.get('uid', None)
        if uid:
            user = User.query.filter_by(id=uid).first()
        if user is None:
            return self.http_response(conf.base.ERROR_CODE_1001)
        return self.http_response(conf.base.ERROR_CODE_0, user.to_json())

    def post(self):
        # TODO: 验证
        args = json_decode(self.request.body)
        user_info: UserInfo = self.current_user.info
        if not user_info:
            user_info = UserInfo()

        for key, value in args.items():
            if key == 'nickname':
                user_info.nickname = args['nickname']
            elif key == 'gender':
                user_info.gender = Gender(args['gender'])

        try:
            image_mates = self.request.files['image']
            user_info.avatar = save_images(image_mates)[0]
        except KeyError:
            pass

        self.current_user.info = user_info
        sessions.commit()
        sessions.close()
