import views.album.album_views as album_views

urls = [
    (r'', album_views.AlbumHandler),
    (r'photo/', album_views.PhotoHandler)
]