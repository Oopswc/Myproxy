# encoding: utf-8
from Proxy import kuai
from Proxy import xici
from Proxy import you
import requests
from Proxy.Test import test_link
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Proxy.DB import db


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

lis = []


def get_ips():
    for ips in kuai.get_iplist() and xici.get_iplist() and you.get_iplist():
        # must insert dict type
        db.insert({"proxy": ips})


if __name__ == "__main__":

    db.delete_all()
    print("\ndb data start:\n")
    get_ips()
    for x in db.find_all():
        print(x["proxy"])

    print(db.find_one())