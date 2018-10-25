from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint

collection = connectMongo()

with open("dummy-fitness.json") as json_data:
    WQ1 = json.load(json_data)
for item in WQ1:
	collection.insert(item)