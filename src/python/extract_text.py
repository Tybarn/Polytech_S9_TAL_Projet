###### Exo 1 : Question 2 #####
import sys
import re

# Check arguments
if len(sys.argv) != 3:
    raise ValueError("Invalid Arguments : Command line should be 'python extract_text.py <input file> <output file>")

# Open input file and create output file
inFile = open(sys.argv[1], 'r')
outFile = open(sys.argv[2], 'w')

# Extract text from ref
for line in inFile:
    words = line.split()
    if len(words) == 0:
        outFile.write('\n')
    else :
        for i in range(0, len(words)-1):
            outFile.write(words[i] + " ")

# Close opened files
inFile.close()
outFile.close()
