import os

import re
import sys

def getWords(line):
	words = line.split()
	if(len(words) < 2):
		return ""
	res = ""
	for i in range(len(words)-2) :
		res += words[i] + " "
	res+= words[-2]
	return res
input = sys.argv[1]

file_in = open(input,"r")
file_ref = open("../data/Exo1/pos_reference.txt.univ")

lines = file_in.readlines()
linesRef = file_ref.readlines()

file_in.close()
file_ref.close()

file_out= open(input+".test","w")
i = 1
construction = getWords(lines[0])
for line in linesRef:
	actualLine = getWords(line)
	print(actualLine)
	words = line.split()
	if(len(words)<=1):
		continue
	while(i < len(lines)-1):
		print("construction "+construction)
		if((construction+getWords(lines[i])).lower()in actualLine.lower()):
			construction+=getWords(lines[i])
			i+=1
		elif((construction+" "+getWords(lines[i])).lower()in actualLine.lower()):
			construction+=" "+getWords(lines[i])
			i+=1
		elif((construction+"'s "+getWords(lines[i])).lower()in actualLine.lower()):
			construction+="'s "+getWords(lines[i])
			i+=1
		elif((construction+"-"+getWords(lines[i])).lower()in actualLine.lower()):
			construction+="-"+getWords(lines[i])
			i+=1
		elif((construction+" Automobile Dealers' Association").lower()in actualLine.lower()):
			construction+=" Automobile Dealers' Association"
			i+=1
		elif((construction+"'s").lower()in actualLine.lower()):
			construction+="'s"
		else:
			file_out.write(actualLine+"\t"+lines[i-1].split()[-1]+"\n")
			construction = getWords(lines[i])
			i += 1
			break
while(i < len(lines)):
	file_out.write(lines[i])
	i+=1

file_out.close()
