from Proxy.log import Log
log = Log("Error")


def check(func):
    def wrapper(self,*args,**kwargs):
        result= func(self,*args,**kwargs)
        if result.status_code == 200:
            return result
        else:
            log.error("Get Response Error")
            pass
    return wrapper