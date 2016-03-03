#!/usr/bin/python
import operator, sys, time

if len(sys.argv) < 3:
	print "Usage is: " +sys.argv[0]+" <input wordlist> <output masklist>"
	sys.exit()

start = time.time()

upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digit=["0","1","2","3","4","5","6","7","8","9"]
masks={}
words=0

with open(sys.argv[1]) as f:
	for word in f:
		mask=""
		for char in word.rstrip('\r\n'):
			if char in upper:
				mask=mask+"?u"
			elif char in lower:
				mask=mask+"?l"
			elif char in digit:
				mask=mask+"?d"
			else:
				mask=mask+"?s"
		if mask not in masks:
			masks[mask] = 1
		else:
			masks[mask] += 1
		words+=1

	sorteddmask = sorted(masks.items(), key=operator.itemgetter(1), reverse=True)

	print "Outputting Data"
	mask_file = open(sys.argv[2],"w")
	for mask in sorteddmask:
		result = mask[0]+","+str(mask[1])+" Occurances,"+str((float(mask[1])/float(words))*100)+"%\n"
		mask_file.write(result)
	mask_file.close()

	runtime=time.time()-start
	print "Total time was " + str(runtime)
	print "Speed was "+str(words/runtime)+" words per second"

	
