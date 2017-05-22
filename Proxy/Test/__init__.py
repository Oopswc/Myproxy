# encoding: utf-8
import requests
from Proxy.error import Linkexception
from Proxy.log import Log
from Proxy.config import URL


log = Log("Test_link")

def test_link(proxy):
    try:
        proxies = {"https": "https://{proxy}".format(proxy=proxy)}
        resp = requests.get(url=URL, proxies=proxies, timeout=10, verify=False)
        resp.raise_for_status
    except Linkexception as e:
        log.error("%s,proxy :%s"%(e, proxy))
    except IOError as e:
        log.error("%s,proxy :%s"%(e, proxy))
    except requests.ProxyError as e:
        log.error("%s,proxy :%s"%(e, proxy))
    except requests.HTTPErrorError as e:
        log.error("%s,proxy :%s"%(e, proxy))
    except requests.TimeoutError as e:
        log.error("%s,proxy :%s"%(e, proxy))
    except requests.ConnectionError as e:
        log.error("%s,proxy :%s"%(e, proxy))
    except requests.ProtocolError as e:
        log.error("%s,proxy :%s"%(e, proxy))
    except:
        pass
    else:
        return True


if __name__ == "__main__":
    # test_link("60.191.170.148:3128")
    proxy = "223.15.29.181:9797"
    proxies = {"https": "https://{proxy}".format(proxy=proxy)}
    resp = requests.get(url=URL, proxies=proxies, timeout=10, verify=False)
    print(resp.status_code)
