from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint

collection = connectMongo()

RQ1 = len(collection.distinct("uid"))
print(RQ1)