# encoding: utf-8
from Proxy.DB.mongodb import Mongo
from Proxy.config import DBNAME, COLLECTION


db = Mongo(DBNAME, COLLECTION)