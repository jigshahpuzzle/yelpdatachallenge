# This file contains scripts to parse data from the Yelp JSON and conduct basic calculations. 


import ast 
import json

# "business" for business data
# "checkin" for checkin data
# "review" for review data
# "tip" for tip data
# "user" for user data
def readData(dataset): 

	if dataset == "business": 
		datafile = open("data/yelp_academic_dataset_business.json", "r")
	elif dataset == "checkin":
		datafile = open("data/yelp_academic_dataset_checkin.json", "r")
	elif dataset == "review":
		datafile = open("data/yelp_academic_dataset_review.json", "r")
	elif dataset == "tip": 
		datafile = open("data/yelp_academic_dataset_tip.json", "r") 
	elif dataset == "user":
		datafile = open("data/yelp_acdaemic_dataset_user.json", "r") 

	data = [] 
	for line in datafile: 
		data.append(json.loads(line))
   
	return data
