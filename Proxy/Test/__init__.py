from Proxy.web.error import check
import requests
import re

url = "https://www.baidu.com"


def test_link(proxy):
    try:
        proxies = {"https":"https://{proxy}".format(proxy = proxy)}
        resp = requests.get(url = url, proxies = proxies,timeout = 10, verify = False)
        print(resp.text)
        print("Proxy :{proxy} is OK.".format(proxy = proxy))
    except:
        pass
