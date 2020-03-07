import os
import re
import sys

# Check input arguments
if len(sys.argv) != 2:
    raise ValueError("Invalid Arguments : Command line should be 'python formulate_lima.py <input file>")

# Open input and output files
outputName = sys.argv[1] + ".univ"
file_in = open(sys.argv[1],"r")
file_out= open(outputName,"w")

# Tranform to univ
p = re.compile('\d+ .*\n')
for line in file_in.readlines():
	words = line.split()
	if(len(words)==0):
		continue
	if('#' not in words[0]): #si la ligne ne commence pas par un chiffre alors on l'ignore
		print(line)
		file_out.write(words[2]+"\t"+words[3]+"\n")

# Close files
file_in.close()
file_out.close()