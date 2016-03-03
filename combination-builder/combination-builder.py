#!/usr/bin/python
import sys
import itertools

if len(sys.argv) < 3:
	print "Usage is: " +sys.argv[0]+" <input wordlist> <input wordlist 2> <additional lists optional>"
	sys.exit()

files = len(sys.argv)-1

listoflists=[]

count=1
while count <= files:
	filearray=[]
	with open(sys.argv[count]) as f:
		for word in f:
			filearray.append(word.rstrip('\r\n'))
	listoflists.append(filearray)
	f.close()
	count=count+1

for list in itertools.product(*listoflists):
	print ''.join(list).replace(" ", "")








