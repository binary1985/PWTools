#!/usr/bin/python
import sys
import itertools

if len(sys.argv) < 3:
	print "Usage is: " +sys.argv[0]+" <input wordlist> <word hamming distance>"
	sys.exit()

dictionary = []
hamming = int(sys.argv[2])

with open(sys.argv[1]) as f:
	for word in f:
		dictionary.append(word.rstrip('\r\n'))

listoflists=[]
count = 0
while count < hamming:
	listoflists.append(dictionary)
	count+=1

for list in itertools.product(*listoflists):
	print ''.join(list).replace(" ", "")
