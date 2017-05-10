# encoding: utf-8
from pymongo import MongoClient
import random
from Proxy.log import Log


class Mongo(object):
    def __init__(self, dbname="test", collection="test", host=None, port=None):
        self.dbn = dbname
        self.coln = collection
        self.client = MongoClient(host, port)
        self.db = self.client[dbname]
        self.collection = self.db[collection]
        self.log = Log(__class__.__name__)

    def insert(self, dict_data):
        if isinstance(dict_data, dict):
            # check existance before insert.
            if not self.is_exist(dict_data):
                self.collection.insert(dict_data)
                self.log.info("Insert dict is :%s" % (str(dict_data)))
        else:
            self.log.info("Error: %s,dict is :%s"%(TypeError, eval(dict_data)))
            raise TypeError

    def delete(self, key, value):
        if value or key:
            if self.collection.delete({key: value}):
                self.log.info("MongoDB delete Error: %s,key is :%s,value is :%s" % ("Not exist", key, value))
        else:
            self.log.error("MongoDB delete Error: %s,key is :%s,value is :%s" % (AttributeError, key, value))
            raise AttributeError

    # find all remarks with key
    def find_all(self):
        for results in self.collection.find():
            yield results

    # find one remark with key
    def find_one(self):
        return random.choice([proxy for proxy in self.find_all()])

    def is_exist(self, dict_data):
        if self.collection.find_one(dict_data):
            self.log.warning("Dict is exist :%s" % (str(dict_data)))
            return True
        else:
            return False

    def delete_all(self):
        self.collection.remove()
        self.log.warning("MongoDB delete all remarks.")

    # function drop_database is belong to MongoClient.A difference between Mongo shell.
    def drop_db(self):
        self.client.drop_database(self.dbn)
        self.log.warning("MongoDB delete db %s."%self.dbn)

    def drop_collection(self):
        self.collection.drop()
        self.log.warning("MongoDB delete collection %s." % self.coln)

if __name__ == "__main__":
    a = {"proxy": "111.222.333.444:1234"}
    print(type(a))

    mg = Mongo()
    mg.insert({"proxy": "1.2.3.4:1234"})
    mg.find_all()
    data = mg.find_one()
    print(data)
    print(mg.is_exist(data))
    mg.delete_all()
    mg.drop_collection()
    mg.drop_db()