#!/usr/bin/python
import sys

if len(sys.argv) < 2:
	print "Usage is: " +sys.argv[0]+" <input wordlist>"
	sys.exit()

upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digit=["0","1","2","3","4","5","6","7","8","9"]
masks={}
words=0
newword=""
with open(sys.argv[1]) as f:
	for word in f:
		newword=""
		mask=""
		for char in word.rstrip('\r\n'):
			if char in upper:
				newword=newword+char
			elif char in lower:
				newword=newword+char
			elif char in digit:
				print newword
			else:
				print newword
