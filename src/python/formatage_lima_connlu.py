import os
import re
import sys

# Check input arguments
if len(sys.argv) != 2:
    raise ValueError("Invalid Arguments : Command line should be 'python formatage_lima.py <input file>")

# Open input and output files
outputName = "ne_test.txt.ne.lima"
file_in = open(sys.argv[1],"r")
file_out= open(outputName,"w")

# Tranform to univ
p = re.compile('\d+ .*\n')
for line in file_in.readlines():
	words = line.split('\t')
	if(len(words)<4):
		continue
	if('#' not in words[0]):
		if("NE=" in words[9]): #si la ligne ne commence pas par un chiffre alors on l'ignore
			file_out.write(words[1]+"\t"+re.findall(r"[\w']+",words[9])[2]+"\n")
		else:
			file_out.write(words[1]+"\tO\n")

# Close files
file_in.close()
file_out.close()
