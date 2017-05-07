# encoding: utf-8

import requests
from lxml import etree
from Proxy.web.error import check
from Proxy.log import Log
PAGE = 5
URL = ("http://www.kuaidaili.com/proxylist/{index}/".format(index = ind) for ind in range(1,PAGE+1))
HEADER = {
    "Accept - Encoding" :"gzip, deflate, sdch, br",
    "Cookie": "",
    "Host" : "sp0.baidu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"" AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
}
XPATH = "//div[@id= 'index_free_list']/table//tbody/tr"


class Kuai(object):
    def __init__(self):
        self.log = Log(__class__.__name__)
        pass

    @staticmethod
    @check
    def get_response(url):
        resp =  requests.get(url=url, headers = HEADER)
        resp.encoding = resp.apparent_encoding
        resp.raise_for_status
        return resp

    def get_iplist(self):
        for url in URL:
            r = self.get_response(url)
            html = etree.HTML(r.text)
            iplist = html.xpath(XPATH)
            for ip in iplist:
                yield ':'.join(ip.xpath("./td/text()")[:2])

if __name__ == "__main__":
    a = Kuai()
    #for x in a.get_iplist():
    #    print(x)
    a.log.info("hello")


