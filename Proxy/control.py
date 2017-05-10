# encoding: utf-8
from Proxy import kuai
from Proxy import xici
from Proxy import you
import requests
from Proxy.Test import test_link
from Proxy.log import Log
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from Proxy.DB import db


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

log = Log("Control")
lis = []


def get_ips():
    for ip in kuai.ips:   #isinstance = generator
        if test_link(ip):
            log.info(ip+" is checkde be useful!")
            # must insert dict type
            db.insert({"proxy": ip})

    for ip in xici.ips:
        if test_link(ip):
            log.info(ip+" is checkde be useful!")
            # must insert dict type
            db.insert({"proxy": ip})
    for ip in you.ips:
        if test_link(ip):
            log.info(ip+" is checkde be useful!")
            # must insert dict type
            db.insert({"proxy": ip})


if __name__ == "__main__":

    db.delete_all()
    print("\ndb data start:\n")
    get_ips()

    for x in db.find_all():
        print(x["proxy"])
    print(db.find_one())