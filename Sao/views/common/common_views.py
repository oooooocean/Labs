import tornado.web
import logging
from common.commons import save_files
import conf.base
import os
from views.base.base_views import BaseHandler
from common.utils import save_images


class UploadHandler(BaseHandler):
    def post(self):
        try:
            image_metas = self.request.files['image']
        except Exception as e:
            logging.error('UploadHandle/post: %r' % (str(e),))
            self.http_response(conf.base.ERROR_CODE_1001)
            return

        if image_metas:
            image_url_list = save_images(image_metas)
            self.http_response(conf.base.ERROR_CODE_0, image_url_list)
        else:
            logging.error('UploadHandle/post: 空图片')
            self.http_response(conf.base.ERROR_CODE_1001)
