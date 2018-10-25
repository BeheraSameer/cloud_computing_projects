# coding: utf-8
from mongo_connect import connectMongo
import constants
import pymongo
import pprint
import sys
import re
import codecs # UniCode support

db = connectMongo()

while True:
	try:
		cmd = raw_input('Waiting For Command: ')
		cmd_parts = cmd.split(" ")
			
		if cmd_parts[0] == "aggiestack" and cmd_parts[1] == "config":
			if cmd_parts[2] == "--hardware" and cmd_parts[3] == "hdwr-config.txt":
			##Read hdwr-config.txt
				try:
					db.collection1.remove({})
					hdwr_data = open("hdwr-config.txt", 'r')
					no_of_racks = hdwr_data.readline().strip()
					##print no_of_racks
					for i in range(int(no_of_racks)):
						line = hdwr_data.readline().strip()
						arr = line.rstrip().split(' ')
						##Create Dictionary Object
						rack_list = { "rack_name" : arr[0], "storage_capacity" : arr[1] }
						##Insert Document into DB
						db.collection1.insert(rack_list)
					no_of_machines = hdwr_data.readline().strip()
					##print no_of_machines
					for i in range(int(no_of_machines)):
						line = hdwr_data.readline().strip()
						arr = line.rstrip().split(' ')
						##Create Dictionary Object
						machine_list = { "mach_name" : arr[0], "rack_name" : arr[1], "ip" : arr[2], "mem" : int(arr[3]), "num_disks" : int(arr[4]), "num_cores" : int(arr[5]) }
						##Insert Document into DBs
						db.collection1.insert(machine_list)
					hdwr_data.close()
						
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "--images" and cmd_parts[3] == "image-config.txt":
			##Read image-config.txt
				try:
					db.collection2.remove({})
					image_data = open("image-config.txt", 'r')
					no_of_images = image_data.readline().strip()
					##print no_of_images
					for i in range(int(no_of_images)):
						line = image_data.readline().strip()
						arr = line.rstrip().split(' ')
						##Create Dictionary Object
						image_list = { "image_name" : arr[0], "image_size" : int(arr[1]), "image_path" : arr[2] }
						##Insert Document into DB
						db.collection2.insert(image_list)
					image_data.close()
						
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "--flavors" and cmd_parts[3] == "flavor-config.txt":
			##Read flavor-config.txt
				try:
					db.collection3.remove({})
					flavor_data = open("flavor-config.txt", 'r')
					no_of_flavors = flavor_data.readline().strip()
					##print no_of_images
					for i in range(int(no_of_flavors)):
						line = flavor_data.readline().strip()
						arr = line.rstrip().split(' ')
						##Create Dictionary Object
						flavor_list = { "flavor_name" : arr[0], "ram_size" : int(arr[1]), "no_of_disks" : int(arr[2]), "no_of_vcpus" : int(arr[3]) }
						##Insert Document into DB
						db.collection3.insert(flavor_list)
					flavor_data.close()
						
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif (cmd_parts[2] not in ["--hardware", "--images", "--flavors"] or cmd_parts[3] not in ["hdwr-config.txt", "image-config.txt", "flavor-config.txt"]):
				print("Input Format Wrong OR Wrong File Name");
				log=open("aggiestack-log.txt","a+")
				log.write(cmd + " " + "--FAILURE\n")
				log.close()	
			
		elif cmd_parts[0] == "aggiestack" and cmd_parts[1] == "show":
			if cmd_parts[2] == "hardware":
			##Display Hardware
				try:
					RQ1 = db.collection1.find()
					for data in RQ1:
						pprint.pprint(data)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "images":
			##Display Images
				try:
					RQ2 = db.collection2.find()
					for data in RQ2:
						pprint.pprint(data)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "flavors":
			##Display Flavors
				try:
					RQ3 = db.collection3.find()
					for data in RQ3:
						pprint.pprint(data)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "all":
			##Display All
				try:
					RQ1 = db.collection1.find()
					for data in RQ1:
						pprint.pprint(data)
					
					RQ2 = db.collection2.find()
					for data in RQ2:
						pprint.pprint(data)
					
					RQ3 = db.collection3.find()
					for data in RQ3:
						pprint.pprint(data)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif (cmd_parts[2] not in ["hardware", "images", "flavors", "all"]):
				print("Input Format Wrong");
				log=open("aggiestack-log.txt","a+")
				log.write(cmd + " " + "--FAILURE\n")
				log.close()
			
		elif cmd_parts[0] == "aggiestack" and cmd_parts[1] == "admin":
			if cmd_parts[2] == "show" and cmd_parts[3] == "hardware":
			##Display Hardware
				try:
					distinct_bad_machs = db.collection5.distinct("bad_mach_name")
					RQ = db.collection1.find({"mach_name": {"$exists": True, "$nin": distinct_bad_machs}},{"mach_name" : 1, "rack_name" : 1, "mem" : 1, "num_disks" : 1, "num_cores" : 1})
					for data in RQ:
						pprint.pprint(data)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif 	cmd_parts[2] == "can_host":
				try:
					machine = cmd_parts[3]
					flavor = cmd_parts[4]
					temp1 = db.collection1.find({"mach_name" : machine},{"mach_name" : 1, "mem" : 1, "num_disks" : 1, "num_cores" : 1})
					if temp1.count() == 0:
						print "No Machine Found With the Given Name"
					if temp1.count() != 0:
						for item in temp1:
							mach_mem = int(item["mem"])
							mach_disks = int(item["num_disks"])
							mach_vcpus = int(item["num_cores"])
					temp2 = db.collection3.find({"flavor_name" : flavor},{"flavor_name" : 1, "ram_size" : 1, "no_of_disks" : 1, "no_of_vcpus" : 1})
					if temp2.count() == 0:
						print "No Flavor Found With the Given Name"
					if temp2.count() != 0:
						for item in temp2:
							flav_mem = int(item["ram_size"])
							flav_disks = int(item["no_of_disks"])
							flav_vcpus = int(item["no_of_vcpus"])
					if (mach_mem >= flav_mem and mach_disks >= flav_disks and mach_vcpus >= flav_vcpus) and temp1.count() != 0 and temp2.count() != 0:
						print("Yes")
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--SUCCESS\n")
						log.close()
					elif temp1.count() == 0 or temp2.count() == 0:
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--FAILURE\n")
						log.close()
					else:
						print("No")
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--SUCCESS\n")
						log.close()
					
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "show" and cmd_parts[3] == "instances":
			##Display Instances
				try:
					RQ = db.collection4.find({},{"instance_name" : 1, "mach_name" : 1, "rack_name" : 1})
					for data in RQ:
						pprint.pprint(data)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "evacuate":
				try:
					rack = cmd_parts[3]
					error_flag = 0
					##Evacuate Rack
					temp = db.collection1.find({"mach_name": {"$exists": True}, "rack_name" : rack},{"mach_name" : 1, "rack_name" : 1})
					if temp.count() == 0:
						print "No Rack Found With the Given Name"
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--FAILURE\n")
						log.close()
					else:
						##Add Unhealthy Racks OR Machines
						for item in temp:
							unhealthy_list = { "bad_rack_name" : item["rack_name"], "bad_mach_name" : item["mach_name"] }
							db.collection5.insert(unhealthy_list)
							distinct_bad_machs = db.collection5.distinct("bad_mach_name")
						for item1 in db.collection4.find({"rack_name" : rack},{"instance_name" : 1, "mach_name" : 1, "rack_name" : 1, "image_name" : 1, "flavor_name" : 1, "flavor_size" : 1, "flavor_disks" : 1, "flavor_vcpus" : 1}):
							found_mach = 0
							bad_rack = (item1["rack_name"])
							bad_mach = (item1["mach_name"])
							instance = (item1["instance_name"])
							image = (item1["image_name"])
							flav_name = (item1["flavor_name"])
							flav_mem = int(item1["flavor_size"])
							flav_disks = int(item1["flavor_disks"])
							flav_vcpus = int(item1["flavor_vcpus"])
							##Assign New Hardware Machine
							for item2 in db.collection1.find({"mach_name": {"$exists": True, "$nin": distinct_bad_machs}},{"mach_name" : 1, "rack_name" : 1, "mem" : 1, "num_disks" : 1, "num_cores" : 1}):
								if (int(item2["mem"]) >= flav_mem and int(item2["num_disks"]) >= flav_disks and int(item2["num_cores"]) >= flav_vcpus):
									instance_list = { "instance_name" : instance, "mach_name" : item2["mach_name"], "rack_name" : item2["rack_name"], "image_name" : image, "flavor_name" : flav_name, "flavor_size" : flav_mem, "flavor_disks" : flav_disks, "flavor_vcpus" : flav_vcpus }
									##Insert New Instance into DB
									db.collection4.insert(instance_list)
									##Update Hardware Machine List
									db.collection1.update(
									{ "mach_name": item2["mach_name"] },
									{ "$inc": { "mem": -flav_mem, "num_disks": -flav_disks, "num_cores": -flav_vcpus } }
									)
									##Update Flag
									found_mach = 1
									break;
								else:
									continue;
							if found_mach == 1:
								print("The VM : " + instance + " Migrated Successfully!")
								##Delete Old Record of Migrated Instance from DB
								db.collection4.remove({ "mach_name": {"$in": distinct_bad_machs}, "instance_name": {"$eq": instance} })
								##Free Old Deprecated Hardware Machine
								db.collection1.update(
								{ "mach_name": bad_mach, "rack_name": bad_rack },
								{ "$inc": { "mem": flav_mem, "num_disks": flav_disks, "num_cores": flav_vcpus } }
								)
							else:
								##Set Error Flag
								error_flag = 1
								print("Sorry! No More Available Resources/Machines for Migration of the VM : " + instance + " Got Deleted")
								##Delete Un-Migrated Instance from DB
								db.collection4.remove({"instance_name": {"$eq": instance} })
								##Free Old Deprecated Hardware Machine
								db.collection1.update(
								{ "mach_name": bad_mach, "rack_name": bad_rack },
								{ "$inc": { "mem": flav_mem, "num_disks": flav_disks, "num_cores": flav_vcpus } }
								)
						if error_flag == 0:
							log=open("aggiestack-log.txt","a+")
							log.write(cmd + " " + "--SUCCESS\n")
							log.close()
						else:
							log=open("aggiestack-log.txt","a+")
							log.write(cmd + " " + "--FAILURE\n")
							log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "remove":
				try:
					mach = cmd_parts[3]
					temp = db.collection1.find({"mach_name": {"$eq": mach}},{"mach_name" : 1, "rack_name" : 1})
					if temp.count() == 0:
						print("No Machine Found With the Given Name")
					for item in temp:
						rm_mach = item["mach_name"]
						rm_rack = item["rack_name"]
					
					##Add Unhealthy Machine
					unhealthy_list = { "bad_rack_name" : rm_rack, "bad_mach_name" : rm_mach }
					db.collection5.insert(unhealthy_list)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "release":
				try:
					good_rack = cmd_parts[3]
					temp = db.collection5.find({"bad_rack_name": {"$eq": good_rack}})
					if temp.count() == 0:
						print ("No Rack Found With the Given Name OR Rack Already Evacuated")
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--FAILURE\n")
						log.close()
					if temp.count() != 0:
						##Remove Rack from Unhealthy List
						db.collection5.remove({"bad_rack_name": {"$eq": good_rack}})
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--SUCCESS\n")
						log.close()
					
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "add" and cmd_parts[3] == ("—mem" or "-mem") and cmd_parts[5] == ("—disk" or "-disk") and cmd_parts[7] == ("—vcpus" or "-vcpus") and cmd_parts[9] == ("-ip" or "—ip") and cmd_parts[11] == ("-rack" or "—rack"):
				try:
					size = int(cmd_parts[4])
					disks = int(cmd_parts[6])
					cores = int(cmd_parts[8])
					ip_addr = cmd_parts[10]
					rack = cmd_parts[12]
					machine = cmd_parts[13]
					temp = db.collection1.find({"rack_name": {"$eq": rack}})
					if temp.count() == 0:
						print("No Rack Found With the Given Name")
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--FAILURE\n")
						log.close()
					if temp.count() != 0:
						##Create Dictionary Object
						machine_list = { "mach_name" : machine, "rack_name" : rack, "ip" : ip_addr, "mem" : size, "num_disks" : disks, "num_cores" : cores }
						##Insert Document into DB
						db.collection1.insert(machine_list)
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--SUCCESS\n")
						log.close()
				except ValueError:
					print("Please Enter an Integer for Size, Disks & Cores")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
		elif cmd_parts[0] == "aggiestack" and cmd_parts[1] == "server":
			if cmd_parts[2] == "create" and cmd_parts[3] == "--image" and cmd_parts[5] == "--flavor":
				try:
					image = cmd_parts[4]
					flavor = cmd_parts[6]
					instance = cmd_parts[7]
					found_machine = 0
					temp1 = db.collection2.find({"image_name": {"$eq": image}})
					temp2 = db.collection3.find({"flavor_name": {"$eq": flavor}})
					if (temp1.count() == 0 or temp2.count() == 0):
						print("No Image OR Flavor Found With the Given Name")
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--FAILURE\n")
						log.close()
					if (temp1.count() != 0 and temp2.count() != 0):
						distinct_bad_machs = db.collection5.distinct("bad_mach_name")
						for item in db.collection3.find({"flavor_name" : flavor},{"flavor_name" : 1, "ram_size" : 1, "no_of_disks" : 1, "no_of_vcpus" : 1}):
							flav_mem = int(item["ram_size"])
							flav_disks = int(item["no_of_disks"])
							flav_vcpus = int(item["no_of_vcpus"])
					
						for item in db.collection1.find({"mach_name": {"$exists": True, "$nin": distinct_bad_machs}},{"mach_name" : 1, "rack_name" : 1, "mem" : 1, "num_disks" : 1, "num_cores" : 1}):
							if (int(item["mem"]) >= flav_mem and int(item["num_disks"]) >= flav_disks and int(item["num_cores"]) >= flav_vcpus):
								instance_list = { "instance_name" : instance, "mach_name" : item["mach_name"], "rack_name" : item["rack_name"], "image_name" : image, "flavor_name" : flavor, "flavor_size" : flav_mem, "flavor_disks" : flav_disks, "flavor_vcpus" : flav_vcpus }
								##Insert Instance into DB
								insert_result = db.collection4.insert(instance_list)
								##Update Hardware Machine List
								db.collection1.update(
								{ "mach_name": item["mach_name"] },
								{ "$inc": { "mem": -flav_mem, "num_disks": -flav_disks, "num_cores": -flav_vcpus } }
								)
								##Update Flag
								found_machine = 1
								break;
							else:
								continue;
						if found_machine == 1:
							log=open("aggiestack-log.txt","a+")
							log.write(cmd + " " + "--SUCCESS\n")
							log.close()
						else:
							print("Sorry! No More Available Resources/Machines")
							log=open("aggiestack-log.txt","a+")
							log.write(cmd + " " + "--FAILURE\n")
							log.close()
					
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "delete":
				try:
					instance = cmd_parts[3]
					temp = db.collection4.find({"instance_name" : instance},{"instance_name" : 1, "mach_name" : 1, "rack_name" : 1, "flavor_name" : 1, "flavor_size" : 1, "flavor_disks" : 1, "flavor_vcpus" : 1})
					if temp.count() == 0:
						print ("No Instance Found With the Given Name")
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--FAILURE\n")
						log.close()
					if temp.count() != 0:
						for item in temp:
							machine = item["mach_name"]
							flav_mem = int(item["flavor_size"])
							flav_disks = int(item["flavor_disks"])
							flav_vcpus = int(item["flavor_vcpus"])
						##Delete Instance from DB
						db.collection4.remove({ "instance_name" : instance })
						##Update Hardware Machine List
						db.collection1.update(
						{ "mach_name": machine },
						{ "$inc": { "mem": flav_mem, "num_disks": flav_disks, "num_cores": flav_vcpus } }
						)
						log=open("aggiestack-log.txt","a+")
						log.write(cmd + " " + "--SUCCESS\n")
						log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
			elif cmd_parts[2] == "list":
				try:
					RQ4 = db.collection4.find({},{"instance_name" : 1, "image_name" : 1, "flavor_name" : 1})
					for data in RQ4:
						pprint.pprint(data)
					
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--SUCCESS\n")
					log.close()
				except:
					print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
					log=open("aggiestack-log.txt","a+")
					log.write(cmd + " " + "--FAILURE\n")
					log.close()
				
		elif cmd_parts[0] == "quit":
			break;	
		else:
			print("Invalid Input");
			log=open("aggiestack-log.txt","a+")
			log.write(cmd + " " + "--FAILURE\n")
			log.close()
		
	except:
		print("Oops! Something Went Wrong!!! - Kindly Check Instruction Manual Again")
		log=open("aggiestack-log.txt","a+")
		log.write(cmd + " " + "--FAILURE\n")
		log.close()