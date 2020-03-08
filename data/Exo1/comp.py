import os
import re
import sys

# Open input and output files
file_in = open("pos_reference.txt.univ","r")
file_out= open("pos_test.txt.pos.lima.univ","r")

# Tranform to univ
linesRef = file_in.readlines()
lignesIn = file_out.readlines()

for i in range(len(linesRef)):
	wordsRef = linesRef[i].split('\t')
	wordsIn = lignesIn[i].split('\t')
	if(wordsRef[0] != wordsIn[0]):
		print(i)
		break

# Close files
file_in.close()
file_out.close()
