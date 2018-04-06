#!/usr/bin/python
import operator, sys, time

if len(sys.argv) < 3:
	print "Usage is: " +sys.argv[0]+" <input wordlist> <output wordlist> <minimum length> <minimum score>"
	sys.exit()

upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digit=["0","1","2","3","4","5","6","7","8","9"]

out_file = open(sys.argv[2],"w")

with open(sys.argv[1]) as f:
	for word in f:
		if len(word.rstrip('\r\n')) < int(sys.argv[3]):
			continue
		score=0
		isup=0
		islo=0
		isdi=0
		issp=0
		for char in word.rstrip('\r\n'):
			if char in upper:
				isup=1
			elif char in lower:
				islo=1
			elif char in digit:
				isdi=1
			else:
				issp=1
		score = isup+islo+isdi+issp
		if score >= int(sys.argv[4]):
			out_file.write(word)

out_file.close()
