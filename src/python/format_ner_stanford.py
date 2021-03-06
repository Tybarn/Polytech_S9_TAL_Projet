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
	origin_tag.append(words[0])
	new_tag.append(words[1])

file_ref.close()

# Structure file to put one word per line
lastTag = 'O'
for line in file_in:
    elmts = line.split()
    for elmt in elmts:
        words = elmt.split('/')
        tag = new_tag[origin_tag.index(words[1])]
        if tag != 'O' and lastTag == tag:
            file_out.write(words[0] + "\t" + new_tag[origin_tag.index(words[1])+1] + "\n")
        else :
            lastTag = tag
            file_out.write(words[0] + "\t" + tag + "\n")
    file_out.write("\n")

# Close files
file_in.close()
file_out.close()