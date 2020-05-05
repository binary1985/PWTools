#!/usr/bin/python
# NTLMmyLM Generate NTLM Wordlist based on LM Cracked Passwords
# Original work by Joshua Platz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os
from itertools import product

def buildcase(istr):
    lst = [(z, z.upper()) if not z.isdigit() else (z,) for z in istr.lower()]
    return ["".join(lstitem) for lstitem in product(*lst)]

if len(sys.argv) < 2:
	print ("Usage: "+sys.argv[0]+" <lm passwords words>")
	sys.exit()

if os.path.isfile(sys.argv[1]) == False:
	print ("Unable to find "+sys.argv[1])
	sys.exit()


with open(sys.argv[1]) as f:
	lines = f.readlines()
	result=[]
	for line in lines:
		if line.rstrip('\r\n') not in result:
			result.append(line.rstrip('\r\n'))
	for line in result:
		items =buildcase(line.rstrip('\r\n'))
		for word in items:
			print (word)
