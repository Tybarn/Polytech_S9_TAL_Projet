import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import sys

file_in = open(sys.argv[1],"r")
file_out= open(sys.argv[2],"w")

text = file_in.read()

text = word_tokenize(text)
ligne = ""
token_tag = pos_tag(text)
for tag in token_tag:
	ligne += tag[0] + "\t" + tag[1] +"\n"
file_out.write(ligne)
file_in.close()
file_out.close()
