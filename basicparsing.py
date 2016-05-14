# This file contains scripts to parse data from the Yelp JSON and conduct basic maniuplations. 


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
# Business data as a list of dictionaries 
# OUTPUT: 
# Dictionary where key = category, value = list of business data 
def catSubset(data):
	subset = {}	
	subset["No Category Listed"] = []
	for business in data: 
		if business["categories"]:
			topcat = business["categories"][0]
			if topcat in subset: 
				subset[topcat].append(business)	
			else: 
				subset[topcat] = [business]
		else: 
			subset["No Category Listed"].append(business) 
	return subset


# DESCRIPTION: 
# Subsets "business" data by city 
# INPUT: 
# Business data as a list of dictionaries 
# OUTPUT: 
# Dictionary where key = city, value = list of business data
def citySubset(data): 
	subset = {} 
	subset["No City Listed"] = [] 
	for business in data: 
		city = business["city"]
		if city: 
			if city in subset: 
				subset[city].append(business)
			else:
				subset[city] = [business]
		else: 
			subset["No City Listed"].append(business)
	return subset		


# DESCRIPTION: 
# Subsets "tips" by business 
# INPUT: 
# Tips data as a list of dictionaries 
# OUTPUT: 
# Dictionary where key = businesss ids, value = list of tips
def tipSubsetBiz(data): 
	subset = {} 
	for tip in data: 
		biz = tip["business_id"]
		if biz in subset: 
			subset[biz].append(tip)
		else: 
			subset[biz] = [tip]

	return subset

# DESCRIPTION: 
# Extracts "business" id and ratings from business data 
# INPUT: 
# Business data as a list of dictionaries 
# OUTPUT: 
# Dictionary where key = business ids, value = average rating 
def bizRatings(data):
	ratings = {} 
	for business in data: 
		stars = business["stars"] 
		if stars:
			ratings[business["business_id"]] = stars

	return ratings 
