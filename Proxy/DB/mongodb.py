from pymongo import MongoClient

conn = MongoClient()
db = conn.MYDATABASE

db.xyz.insert({"name":"joke","age":25,"home":"CHN"})