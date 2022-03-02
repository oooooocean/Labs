import tornado.ioloop
import tornado.options
import app

if __name__ == '__main__':
    print('🚀')
    tornado.options.parse_command_line()
    app.Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.current().start()
    print('END SERVE')