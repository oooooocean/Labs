import tornado.web as web
import os.path as path
from common.url_router import url_wrapper, include


class Application(web.Application):
    def __init__(self):
        handlers = url_wrapper([
            (r'/users/', include('views.users.users_urls'))
        ])
        settings = dict(
            debug=True,
            static_path=path.join(path.dirname(__file__), 'static'),
            template_path=path.join(path.dirname(__file__), 'templates')
        )
        super().__init__(handlers, **settings)
