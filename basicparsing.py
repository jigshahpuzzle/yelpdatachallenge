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
# Subsets "tip" OR "review" by business 
# INPUT: 
# Tip OR Review data as a list of dictionaries 
# OUTPUT: 
# Dictionary where key = businesss ids, value = list of tip OR review
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


# DESCRIPTION:
# Computes hours open per business
# INPUT: 
# Business data as a list of dictionaries 
# OUTPUT:
# Dictionary where key = business id, value = hours open weekly
def bizHours(data): 
	hours = 0
	bizDict = {}
	for business in data: 
		hours = 0
		b_id = business["business_id"]
		opendata = business["hours"]	
		if opendata: 
			for day in opendata:
				opent = int(opendata[day]["open"][0:2])
				closet = int(opendata[day]["close"][0:2])
				if closet < 12:
					closet += 24
				hours += closet - opent
		if hours == 0:
			bizDict[b_id] = "N/A"
		else: 
			bizDict[b_id] = hours			
	return bizDict	

# *** TO BE COMPLETED ***
# DESCRIPTION: 
# Computes basic statistics on the business data
# INPUT: 
# Business data as a list of dictionaries 
# OUTPUT: 
# Dictionary where key = stat name, value = stat value
def bizStats(data): 
	statsDict = {}
	ratingList = [] 	
	reviewCountList = []
	hours = []
	hoursDict = bizHours(data) 
	attributes = {} 
	ambiences = {}
	for b_id, hour in hoursDict.iteritems(): 
		hours.append(hour)

	for business in data: 
		rating = business["stars"]
		rc = business["review_count"]
		atts = business["attributes"]
		for att in atts: 
			if att in attributes: 
				if atts[att] == True:
					attributes[att]["True"] += 1
				else: 
					attributes[att]["False"] += 1 
			else: 
				attributes[att] = {}
				attributes[att]["True"] = 0 
				attributes[att]["False"] = 0
				if atts[att] == True: 
					attributes[att]["True"] += 1
				else:		
					attributes[att]["False"] += 1
	

		if rating:
				ratingList.append(rating) 
		if rc:
			reviewCountList.append(rc)
	
	print ratingList
	print hours
	print reviewCountList	
	print attributes
	print ambiences
	return statsDict

# DESCRIPTION
# Computes total check-ins for a business 
# INPUT: 
# Check-In Data as a list of dictionaries 
# OUTPUT: 
# Total # of checkins
def processCheckins(data):
	total = 0
	for key1 in data: 
		for key2 in data[key1]: 
			total += data[key1][key2]
	return total
