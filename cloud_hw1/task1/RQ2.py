from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint

collection = connectMongo()

RQ2 = collection.find({"tags":"active"},{"uid": 1})
for data in RQ2:
	pprint.pprint(data)