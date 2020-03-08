import os

import re
import sys


file_ref = open(sys.argv[1],"r")
file_in = open(sys.argv[2],"r")
file_out= open(sys.argv[3],"w+")

limited_tag = []
ref_tag = []

print("Convertion")

for line in file_ref.readlines():
	words = line.split()
	limited_tag.append(words[0])
	ref_tag.append(words[1])

file_ref.close()

for line in file_in.readlines():
	words = line.split()
	file_out.write(words[0]+"\t"+ref_tag[limited_tag.index(words[1])]+"\n")

file_in.close()
file_out.close()
