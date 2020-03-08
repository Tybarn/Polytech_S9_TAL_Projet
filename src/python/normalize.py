import os
import re
import sys

# Check input arguments
if len(sys.argv) != 3:
    raise ValueError("Invalid Arguments : Command line should be 'python normalize.py <input file> <ref file>")

# Open files
input = sys.argv[1]
input_ref = sys.argv[2]
file_ref = open(input_ref,"r")
file_in = open(input,"r")

# Get all line from input file and close
inputLines = []
for line in file_in:
    if line.split('\t')[0] != '\n':
        inputLines.append(line)
file_in.close()

# input file as output file
file_out = open(sys.argv[1], 'w')

# Compare files and create result
resWords = []
resValues = []
inputLinesIndex = -1
for line in file_ref:
    refWords = line.split('\t')
    if refWords[0] == '\n':
        for i in range(0, len(resWords)):
            file_out.write(resWords[i] + '\t' + resValues[i])
        file_out.write('\n')
        resWords = []
        resValues = []
    else:
        inputLinesIndex += 1
        tmpWord = inputLines[inputLinesIndex].split('\t')[0]
        refWordTmp = refWords[0].replace(" ", "")
        while tmpWord != refWordTmp and tmpWord != "''" and refWordTmp != "\"":
            inputLinesIndex += 1
            tmpWord += inputLines[inputLinesIndex].split('\t')[0]
        resWords.append(refWords[0])
        resValues.append(inputLines[inputLinesIndex].split('\t')[1])

# Close files
file_ref.close()
file_out.close()