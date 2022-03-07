import tornado.web
import logging
from common.commons import http_response, save_files
import conf.base
import os


class UploadHandle(tornado.web.RequestHandler):
    def post(self):
        try:
            image_metas = self.request.files['image']
        except Exception as e:
            logging.error('UploadHandle/post: %r' % (str(e),))
            http_response(self, conf.base.ERROR_CODE_1001)
            return

        if image_metas:
            cwd = os.getcwd()
            save_image_path = os.path.join(cwd, 'static/upload/')
            file_name_list = save_files(image_metas, save_image_path)
            image_url_list = [conf.base.SERVER_HOST + '/static/upload/' + i for i in file_name_list]
            http_response(self, conf.base.ERROR_CODE_0, image_url_list)
        else:
            logging.error('UploadHandle/post: 空图片')
            http_response(self, conf.base.ERROR_CODE_1001)