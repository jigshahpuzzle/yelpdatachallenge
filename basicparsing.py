# This file contains scripts to parse data from the Yelp JSON and conduct basic calculations. 


import json

# DESCRIPTION:
# Reads data in from "data" directory 
# INPUT: 
# "business" for business data
# "checkin" for checkin data
# "review" for review data
# "tip" for tip data
# "user" for user data
# OUTPUT: 
# List of Dictionaries where each dict is a converted json object
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


# DESCRIPTION: 
# Subsets "business" data by top category of business 
# INPUT: 
# Data as a list of dictionaries 
# OUTPUT: 
# Dictionary where key = category, value = business data 
def catSubset(data):
	subset = {}	
	subset["No Category Listed"] = []
	for business in data: 
		if business["categories"]:
			topcat = business["categories"][0]
			if topcat in subset: 
				subset[topcat].append(business)	
			else: 
				subset[topcat] = []
		else: 
			subset["No Category Listed"].append(business) 
	return subset 
