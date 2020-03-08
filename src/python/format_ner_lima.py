###### Exo 2 : Question 4 #####
import os
import re
import sys

# Check input arguments
if len(sys.argv) != 3:
    raise ValueError("Invalid Arguments : Command line should be 'python formatage_stanford.py <input file> <POSTags file>")

# Open files
input = sys.argv[1]
input_ref = sys.argv[2]
output = sys.argv[1] + ".conll"
file_ref = open(input_ref,"r")
file_in = open(input,"r")
file_out= open(output,"w")

# Get tags and make library
origin_tag = []
new_tag = []

for line in file_ref.readlines():
	words = line.split()
	if(len(words)>1):
		origin_tag.append(words[0])
		new_tag.append(words[1])

file_ref.close()

# Structure file to put one word per line
lastTag = 'O'
for line in file_in.readlines():
	elmts = line.split()
	if(len(elmts) <= 1):
		continue
	tag = new_tag[origin_tag.index(elmts[-1])]
	for word in elmts[:-2]:
		file_out.write(word + " ")
	file_out.write(elmts[-2]+"\t")
	if tag != 'O' and lastTag == tag:
		file_out.write(new_tag[origin_tag.index(elmts[-1])+1] + "\n")
	else :
		lastTag = tag
		file_out.write(tag + "\n")

# Close files
file_in.close()
file_out.close()