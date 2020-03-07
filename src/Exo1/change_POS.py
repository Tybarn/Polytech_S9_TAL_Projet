###### Exo 1 : Question 1 #####
import os
import re
import sys

# Check input arguments
if len(sys.argv) != 4:
    raise ValueError("Invalid Arguments : Command line should be 'python change_POS.py <input file> <output file> <POSTags file>")

# Open files
input = sys.argv[1]
input_ref = sys.argv[3]
output = sys.argv[2]
file_ref = open(input_ref,"r")
file_in = open(input,"r")
file_out= open(output,"w")

# Get univ tags and make library
origin_tag = []
new_tag = []

for line in file_ref.readlines():
	words = line.split()
	origin_tag.append(words[0])
	new_tag.append(words[1])

file_ref.close()

# Format input file to univ
for line in file_in.readlines():
	# Get words in line
	words = line.split()
	if(len(words)==0):
		file_out.write("\n")
		continue
	# Write convert line in output file
	for i in range(0,len(words)-1):
		if i == len(words)-2 :
			file_out.write(words[i])
		else:
			file_out.write(words[i] + " ")
	file_out.write("\t" + new_tag[origin_tag.index(words[-1])] + "\n")

# Close files
file_in.close()
file_out.close()