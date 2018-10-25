from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint

collection = connectMongo()



RQ4 = collection.aggregate([
   {
     '$project': {
       "activityDurationTotal": { '$sum': "$activityDuration"}
     }
   }
])

for data in RQ4:
	pprint.pprint(data)