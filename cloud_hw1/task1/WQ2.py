from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint

collection = connectMongo()

collection.update(
   { 'uid': 1001 },
   {
     '$set': {
       'height': "5ft10in",
       'weight': "190lbs",
       'tags': [ "ambitious" ]
       }
   }
)