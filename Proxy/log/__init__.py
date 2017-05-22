import os
import logging
from logging.handlers import TimedRotatingFileHandler
from Proxy.config import DEBUG, INFO, ERROR


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')

LEVEL = DEBUG
FORMATTER = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'


class Log(logging.Logger):
    def __init__(self, name="Default", level=DEBUG):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=self.level)
        self.__setFileHandler__(self.level)
        self.__setStreamHandler__(self.level)

    def __setFileHandler__(self, level=None):
        file_name = os.path.join(LOG_PATH, '{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=15)
        file_handler.suffix = '%Y%m%d.log'
        file_handler.setFormatter(logging.Formatter(FORMATTER))

        if not level:
            file_handler.setLevel(LEVEL)
        else:
            file_handler.setLevel(self.level)

        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(FORMATTER))

        if not level:
            stream_handler.setLevel(LEVEL)
        else:
            stream_handler.setLevel(self.level)

        self.addHandler(stream_handler)


if __name__ == "__main__":
    log = Log()
    log.info("look at me")
    log = Log(name="Default", level=INFO)
    log.info("look at me")