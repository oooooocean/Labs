from views.base.base_views import AuthBaseHandler
from common.exception import ERROR_CODE_1001, ERROR_CODE_0, SaoException
from models.album_model import Album, Photo
from service.utils import save_images
from time import time
from service.paginate import paginate


class PhotoHandler(AuthBaseHandler):
    def get(self):
        """
        指定相册内的所有图片
        :return:
        """
        try:
            album_id = self.get_query_argument('album_id')
            self.success(paginate(self, Photo, Photo.album_id == album_id))
        except AssertionError as e:
            raise SaoException(msg=e.__str__(), code=1001)
        except Exception:
            raise ERROR_CODE_1001

    def post(self):
        """
        添加图片
        :return:
        """
        try:
            album_id = self.get_body_argument['album_id']
            album = Album.query.filter(Album.id == album_id).first()
            assert album
            image_metas = self.request.files.get('image', None)
            assert len(image_metas) > 0
        except Exception:
            raise ERROR_CODE_1001
        else:
            image_names = [mate.get('filename') for mate in image_metas]
            image_url_list = save_images(image_metas)
            photos = [Photo(album_id=album.id, name=image_name, create_time=int(time()))
                      for image_name in image_names]
            Photo.saveAll(photos)
            self.success(image_url_list)

    def delete(self):
        """
        删除图片
        :return:
        """
        try:
            delete_ids = self.json_args['delete_ids']
            assert len(delete_ids) > 0
        except Exception:
            raise ERROR_CODE_1001
        else:
            deleted_count = Photo.query.filter(Photo.id in delete_ids).delete()
            self.success(deleted_count)
