from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint

import redis

collection = connectMongo()

dir(redis)

r = redis.Redis()
subscribing = False;
topic = "";

while True:
	try:
		if subscribing:
			print("Subscribed")
			for item in p.listen():	
				print(item)
		cmd = raw_input('Waiting For Command: ')
		print(cmd)
		cmd_parts = cmd.split(" ")
		cmd_parts[0] = cmd_parts[0].lower()
		print(cmd_parts)
		if cmd_parts[0] == "select":
			topic = cmd_parts[1].strip(' \t\n\r')
		elif cmd_parts[0] == "read" and topic != "":
			RQ = collection.find({ "_id": topic })
			for data in RQ:
				pprint.pprint(data)
			##res = r.lrange(topic, 0, -1) 
			##print res
		elif cmd_parts[0] == "read" and topic == "":
			print("No Message Board Selected to Read")
		elif cmd_parts[0] == "write" and topic != "":
			to_set = (' '.join(cmd_parts[1:])).strip(' \t\n\r')
			##r.rpush(topic, to_set)
			##res = r.publish(topic, to_set) 
			##print res
			if to_set != "":
				try:
					collection.insert([{ '_id' : topic, '_msgs' : [to_set] }])
					res = r.publish(topic, to_set) 
					print res
				except:
					collection.update(
					{ "_id": topic },
					{ '$push': { "_msgs": to_set } }
					)
					res = r.publish(topic, to_set) 
					print res
			else:
				print("No Message - Please Try Again")
		elif cmd_parts[0] == "write" and topic == "":
			print("No Message Board Selected to Write")
		elif cmd_parts[0] == "listen" and topic != "":
			subscribing = True;
			p = r.pubsub()
			res = p.subscribe([topic]) 
			print res
		elif cmd_parts[0] == "listen" and topic == "":
			print("No Message Board Selected to Listen")
		elif cmd_parts[0] == "flush" and topic != "":
			r.flushdb()
			collection.remove({"_id": topic})
			print("Message Board and RAM Cleared")
		elif cmd_parts[0] == "flush" and topic == "":
			print("No Message Board Selected to Clean")
		elif cmd_parts[0] == "reset":
			topic = ""
		elif cmd_parts[0] == "quit":
			break;
		else:
			print("Input Format Wrong");

	except KeyboardInterrupt:
		subscribing = False
	except:
		print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")