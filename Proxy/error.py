# encoding: utf-8
from Proxy.log import Log

log = Log("Error")


def check(func):
    def wrapper(self, *args, **kwargs):
        result= func(self, *args, **kwargs)
        if result.status_code == 200:
            return result
        else:
            log.error("Get Response Error in function :%s."%func.__name__)
            pass
    return wrapper


class Linkexception(Exception):
    def __init__(self, err="Link test error"):
        Exception.__init__(self, err)
