import tornado.ioloop
import tornado.options
import app
import conf.logger
from conf.db import init_db

if __name__ == '__main__':
    print('🚀')
    conf.logger.config_log()
    init_db()
    tornado.options.parse_command_line()
    app.Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.current().start()
    print('END SERVE')