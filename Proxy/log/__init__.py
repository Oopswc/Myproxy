import os
import logging
from logging.handlers import TimedRotatingFileHandler

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')

LEVEL = logging.DEBUG
FORMATTER = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'


class Log(logging.Logger):
    def __init__(self, name = "Default"):
        self.name = name
        self.level = LEVEL
        logging.Logger.__init__(self, self.name, level=self.level)
        self.setFileHandler()
        self.setStreamHandler()

    def setFileHandler(self, level=None):
        file_name = os.path.join(LOG_PATH, '{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=15)
        file_handler.suffix = '%Y%m%d.log'
        file_handler.setFormatter(logging.Formatter(FORMATTER))

        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)

        self.addHandler(file_handler)

    def setStreamHandler(self, level=None):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter(FORMATTER))

        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)

        self.addHandler(stream_handler)


if __name__ =="__main__":
    log = Log()
    log.info("look at me")