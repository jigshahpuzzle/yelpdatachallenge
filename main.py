import basicparsing as bp

if __name__ == "__main__":
	obj = bp.readData("tip")
	obj = bp.tipSubsetBiz(obj)		
	for business, tips in obj.iteritems():
		print business, tips
