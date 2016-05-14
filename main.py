import basicparsing as bp

if __name__ == "__main__":
	obj = bp.readData("business")
	obj = bp.catSubset(obj)	
	print obj
