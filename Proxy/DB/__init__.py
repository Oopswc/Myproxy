from Proxy.DB.mongodb import Mongo

DBNAME = "database"
COLLECTION = "proxy"

db = Mongo(DBNAME, COLLECTION)