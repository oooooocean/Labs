import views.album.album_views as album_views
import views.album.photo_views as photo_views

urls = [
    (r'', album_views.AlbumHandler),
    (r'photo/', photo_views.PhotoHandler)
]