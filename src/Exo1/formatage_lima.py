import os

import re
import sys

input = "pos_test.txt.pos.lima"
output = "pos_test.txt.pos.lima.univ"

file_in = open(input,"r")
file_out= open(output,"w")

p = re.compile('\d+ .*\n')
for line in file_in.readlines():
	words = line.split()
	if(len(words)==0):
		continue
	if('#' not in words[0]): #si la ligne ne commence pas par un chiffre alors on l'ignore
		print(line)
		file_out.write(words[2]+"\t"+words[3]+"\n")

file_in.close()
file_out.close()