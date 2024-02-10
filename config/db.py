import urllib
from pymongo import MongoClient

username = urllib.parse.quote_plus('fastApi')
password = urllib.parse.quote_plus('fastApi@123')
client = MongoClient('mongodb+srv://%s:%s@fastapi.hkm8kte.mongodb.net' % (username, password))

db = client.fastDemo
collection_name = db["fastDemo"]
