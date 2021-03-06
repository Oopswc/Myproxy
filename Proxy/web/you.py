# encoding: utf-8

import requests
import re
from lxml import etree
from Proxy.log import Log

PAGE = 5   #page <= 5
start_url = "http://www.youdaili.net/Daili/http/"

HEADER = {
    "Accept - Encoding":"gzip, deflate, sdch, br",
    "Cookie": "",
    "Host": "www.youdaili.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"" AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
}
XPATH = "//div[@class='chunlist']/ul/li[1]/p/a/@href"


class You(object):
    def __init__(self):
        self.log = Log(__class__.__name__)
        pass

    @staticmethod
    def get_response(url):
        resp = requests.get(url=url, headers = HEADER)
        resp.encoding = resp.apparent_encoding
        resp.raise_for_status
        return resp

    @property
    def ips(self):
        lis = []
        start_resp = self.get_response(start_url)
        try:
            html = etree.HTML(start_resp.text)
        except AttributeError as e:
            self.log.error("Response is None,ErrorType:%s" % e)
        else:
            parse_url = html.xpath(XPATH)[0]
            num = re.search("\d+",parse_url)
            link = re.sub("\d+",num.group(0)+"_{index}",parse_url)
            urls = (link.format(index=ind) for ind in range(2, PAGE + 1))

            r = self.get_response(parse_url)
            try:
                lis = lis + re.findall("(?:\d{1,3}\.){3}\d{1,3}\:\d{1,4}", r.text)
            except AttributeError as e:
                self.log.error("Response is None,ErrorType:%s" % e)
            else:
                for url in urls:
                    r = self.get_response(url)
                    lis = lis + re.findall("(?:\d{1,3}\.){3}\d{1,3}\:\d{1,4}",r.text)
                for x in lis:
                    self.log.info("Find:%s" % x)
                    yield x


if __name__ == "__main__":
    a = You()
    for x in a.get_iplist():
        print(x)



