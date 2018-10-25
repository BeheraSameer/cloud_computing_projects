from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint

collection = connectMongo()

RQ3 = collection.find({"goal.stepGoal": { '$gt': 5000 }},{"uid": 1})
for data in RQ3:
	pprint.pprint(data)