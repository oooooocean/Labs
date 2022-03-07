import logging
from logging.handlers import TimedRotatingFileHandler, SysLogHandler


def config_log():
    logging.basicConfig(level=logging.DEBUG)

    log_file_path = 'log/log.log'
    logger = logging.getLogger()

    handler = TimedRotatingFileHandler(log_file_path, when='D', interval=1, backupCount=30)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', )
    handler.setFormatter(formatter)
    handler.setLevel(logging.ERROR)
    logger.addHandler(handler)
