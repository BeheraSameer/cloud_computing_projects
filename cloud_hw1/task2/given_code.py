import redis

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

			topic = cmd_parts[1]

		elif cmd_parts[0] == "read" and topic != "":

			res = r.lrange(topic, 0, -1) 

			print res

		elif cmd_parts[0] == "read" and topic == "":

			print("No Message Board Selected")

		elif cmd_parts[0] == "write" and topic != "":

			to_set = ' '.join(cmd_parts[1:])

			r.rpush(topic, to_set)

			res = r.publish(topic, to_set) 

			print res

		elif cmd_parts[0] == "write" and topic == "":

			print("No Message Board Selected")

		elif cmd_parts[0] == "listen" and topic != "":

			subscribing = True;

			p = r.pubsub()

			res = p.subscribe([topic]) 

			print res

		elif cmd_parts[0] == "listen" and topic == "":

			print("No Message Board Selected")

		elif cmd_parts[0] == "flush":

			r.flushdb()

		elif cmd_parts[0] == "quit":

			break;

		else:

			print("Input Format Wrong");



	except KeyboardInterrupt:

		subscribing = False