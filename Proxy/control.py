# encoding: utf-8
from Proxy import kuai
from Proxy import xici
from Proxy import you
import requests
from Proxy.Test import test_link
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

lis = []

def get_ips():
    for ips in kuai.get_iplist() and xici.get_iplist() and you.get_iplist():
        print(ips)
        try:
            proxies = {"http": "http://{proxy}".format(proxy=ips),"https":"https://{proxy}".format(proxy = ips)}
            resp = requests.get(url="https://www.baidu.com", proxies=proxies, timeout=10, verify=False)
            print(resp)
            print("Proxy :{proxy} is OK.".format(proxy=ips))
            lis.append(ips)
        except:
            print(ips+"is error.")


get_ips()

for x in lis:
    print(x)