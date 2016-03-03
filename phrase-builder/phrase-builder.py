#!/usr/bin/python
import sys,string


if len(sys.argv) < 4:
	print "Usage is: " +sys.argv[0]+" <input file> <output file> <word hamming distance>"
	sys.exit()


phrases=[]
f = open(sys.argv[1])
for word in f.read().split():
	phrases.append(word)


hamming = int(sys.argv[3])
phraselength=len(phrases)
count = 0

phrase_file = open(sys.argv[2],"w")
while count <= (phraselength):
	try:
		counthamming = 0
		hammedphrase = ""
		while counthamming < hamming:
			hammedphrase = hammedphrase + phrases[count+counthamming]
			counthamming=counthamming+1
		hammedphrase = hammedphrase.translate(string.maketrans("",""), string.punctuation)
		phrase_file.write(hammedphrase.lower()+"\n")
		count = count + 1
	except:
		pass
		count = count + 1
phrase_file.close()