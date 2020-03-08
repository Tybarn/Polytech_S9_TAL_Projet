import os

import re
import sys

input = sys.argv[1]

file_in = open(input,"r")

lines = file_in.readlines()

print(lines)
file_in.close()

file_out= open(input,"w")

for line in lines:
	words = line.split()
	if(len(words)==0):
		continue
	print(line)
	print(words[:-1])
	for word in words[:-1]: 
		file_out.write(word+"\t"+words[-1]+"\n")

file_out.close()
