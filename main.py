import basicparsing as bp

if __name__ == "__main__":
	obj = bp.readData("business")
	obj = bp.bizHours(obj)	
	for key, value in obj.iteritems():
		print key, value	
