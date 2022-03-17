from views.base.base_views import AuthBaseHandler
from common.exception import ERROR_CODE_1001, ERROR_CODE_0, ERROR_CODE_1005
from models.album_model import Album, Photo
from service.utils import save_images
from conf.db import sessions
from time import time


class AlbumHandler(AuthBaseHandler):
    def get(self):
        """
        用户的所有相册或指定相册
        :return:
        """

        id = self.get_query_argument('id', None)
        if id:
            album = Album.query.filter(Album.id == id).first()
            if album:
                self.http_response(ERROR_CODE_0, album.to_json())
            else:
                self.http_response(ERROR_CODE_1001)
        else:
            albums = Album.query.filter(Album.user_id == self.current_user.id).all()
            albums_json = [album.to_json() for album in albums]
            self.http_response(ERROR_CODE_0, albums_json)

    def post(self):
        """
        修改相册
        :return:
        """
        try:
            album_id = self.json_args['album_id']
            name = self.json_args['name']
        except Exception:
            raise ERROR_CODE_1001
        else:
            album = Album.query.filter(Album.id == album_id).first()
            if not album:
                raise ERROR_CODE_1001
            album.name = name
            album.save()
            self.http_response(ERROR_CODE_0, album.id)

    def put(self):
        """
        新增
        :return:
        """
        try:
            name = self.json_args['name']
        except Exception:
            raise ERROR_CODE_1001
        else:
            exist = Album.query.filter(Album.user_id == self.current_user.id, Album.name == name).limit(1)
            if exist:
                raise ERROR_CODE_1005
            album = Album(name=name, user_id=self.current_user.id, create_time=int(time()))
            album.save()
            self.http_response(ERROR_CODE_0, album.id)

    def delete(self):
        """
        删除
        :return:
        """
        try:
            album_id = self.json_args.get['id']
        except Exception:
            raise ERROR_CODE_1001
        else:
            Album.query.filter(Album.id == album_id).delete()
            self.http_response(ERROR_CODE_0)


class PhotoHandler(AuthBaseHandler):
    def get(self):
        """
        指定相册内的所有图片
        :return:
        """
        try:
            album_ids = self.get_query_arguments['album_ids']
        except Exception:
            raise ERROR_CODE_1001
        else:
            result = {album_id: [photo.to_json() for photo in Photo.query.filter(Photo.album_id == album_id).all()]
                      for album_id in album_ids}
            self.success(result)

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
