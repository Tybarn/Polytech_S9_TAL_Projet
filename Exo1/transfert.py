import os

import re
import sys

input = "pos_reference.txt.lima"
input_ref = "POSTags_PTB_Universal_Linux.txt"
output = "pos_reference.txt.univ"

file_ref = open(input_ref,"r")
file_in = open(input,"r")
file_out= open(output,"w")

limited_tag = []
ref_tag = []

for line in file_ref.readlines():
	words = line.split()
	limited_tag.append(words[0])
	ref_tag.append(words[1])

file_ref.close()

for line in file_in.readlines():
	words = line.split()
	if(len(words)==0):
		continue
	print(words)
	for i in range(0,len(words) -2):
		file_out.write(words[i]+" ")
	if(words[-1]=="SCONJ"):
		words[-1]="CC"
	elif(words[-1]=="SENT"):
		words[-1]="."
	elif(words[-1]=="COMMA"):
		words[-1]=","
	elif(words[-1]=="COLON"):
		words[-1]=":"
	elif (words[-1]=="AUX"):
		words[-1]="MD"
	elif (words[-1]=="PROPN"):
		words[-1]="NNP"
	elif(words[-1]=="ADJ"):
		words[-1]="JJ"
	elif(words[-1]=="VERB"):
		words[-1]="VB"
	elif(words[-1]=="DET"):
		words[-1]="DT"
	elif(words[-1]=="ADP"):
		words[-1]="IN"
	elif(words[-1]=="NOUN"):
		words[-1]="NN"
	elif(words[-1]=="PART"):
		words[-1]="POS"
	elif(words[-1]=="CONJ"):
		words[-1]="CC"
	elif(words[-1]=="OQU"):
		words[-1]="."
	elif(words[-1]=="QUOT"):
		words[-1]="."
	elif(words[-1]=="OPAR"):
		words[-1]="."
	elif(words[-1]=="CPAR"):
		words[-1]="."
	
	file_out.write("_"+ref_tag[limited_tag.index(words[-1])]+"\n")

file_in.close()
file_out.close()