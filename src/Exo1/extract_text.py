###### Exo 1 : Question 2 #####
import sys
import re

# Check arguments
if len(sys.argv) != 3:
    raise ValueError("Invalid Arguments : Command line should be 'python extract_text.py <input file> <output file>")

# Open input file and create output file
inFile = open(sys.argv[1], 'r')
outFile = open(sys.argv[2], 'w')

# Get sentence and build text
word = ''
sentence = ''
for line in inFile:
    if line != '\n':
        # find first column
        splitLine = line.split('\t')
        word = splitLine[0]
        # Add it to sentence variable
        sentence += word + ' '
    else:
        outFile.write(sentence + "\n")
        sentence = ''
if sentence != '':
    outFile.write(sentence + "\n")
    sentence = ''

# Close opened files
inFile.close()
outFile.close()
