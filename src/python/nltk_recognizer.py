import nltk
from nltk.corpus import state_union
from nltk.tokenize import RegexpTokenizer
from nltk import RegexpParser
import sys
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

inFile = open(sys.argv[1],'r')
sample_text = inFile.read()


def extract_entities(corpus, fichierSortie):
    print("Text :\n")
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(corpus)
    print("After tokenize:\n")    
    print(words)
    token_tag = nltk.pos_tag(words)
    print("After pos tag:\n")
    print(token_tag)
    patterns = """Compound: {<DT>?<JJ>*<NN>}"""
    chunked = RegexpParser(patterns)
    print("After regex :\n")
    output = chunked.parse(token_tag)
    print(output)
    print("After token :\n")
    print(token_tag)
    output_ne = nltk.ne_chunk(token_tag)
    print("After named entity recognition")
    print(output_ne)
    outFile = open(fichierSortie+"-tmp",'w+')
    outFile.write(str(output_ne));
    outFile.close()
    return output_ne


words_named = extract_entities(sample_text,sys.argv[2])

def ref_entities():
    print("Named Entities:\n")
    outFilePos = open(sys.argv[2],"w+")
    print("Open file")
    fp = open(sys.argv[2]+"-tmp","r")
    print("open temp file")
    lines = fp.readlines()
    for line in lines[1:-1]:
        line = line[2:-1]
        mot1_parser = ["",""]
        mot2_parser = ["",""]
        mot3_parser = ["",""]
        if line[0] == "(":
            line = line[1:]
        if line[len(line)-1] == ")":
            line = line[:-1]
        if line[len(line)-1] == ")":
            line = line[:-1]
        if "ORGANIZATION" in line:
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
        elif "PERSON" in line:
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
        elif "LOCATION" in line:  
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
        elif "DATE" in line or "TIME" in line or "MONEY" in line or "PERCENT" in line or "FACILITY" in line or "GPE" in line:
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
        else:
            line_parser = line.split("/")
            mot1_parser[0]=line_parser[0]
            mot1_parser[1]=line_parser[1]
        outFilePos.write(mot1_parser[0]+"\t"+mot1_parser[1]+"\n")
        print(mot1_parser[0]+"/"+mot1_parser[1])
        if mot2_parser[1] != "":
            outFilePos.write(mot2_parser[0]+"\t"+mot2_parser[1]+"\n")
            print(mot2_parser[0]+"/"+mot2_parser[1])
        if mot3_parser[1] != "":
            outFilePos.write(mot3_parser[0]+"\t"+mot3_parser[1]+"\n")
            print(mot3_parser[0]+"/"+mot3_parser[1])
    fp.close()
    outFilePos.close()

ref_entities()


def named_entities(words_named):
    print("Named Entities:\n")
    outFile = open(sys.argv[2],"w+")
    print("Open file")
    fp = open(sys.argv[2]+"-tmp","r")
    print("open temp file")
    lines = fp.readlines()
    for line in lines[1:-1]:
        line = line[2:-1]
        mot1_parser = ["",""]
        mot2_parser = ["",""]
        mot3_parser = ["",""]
        if line[0] == "(":
            line = line[1:]
        if line[len(line)-1] == ")":
            line = line[:-1]
        if line[len(line)-1] == ")":
            line = line[:-1]
        if "ORGANIZATION" in line:
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            mot1_parser[1] = "B-ORG"
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
                mot2_parser[1]="I-ORG"
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
                mot3_parser[1]="I-ORG"
        elif "PERSON" in line:
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            mot1_parser[1]="B-PERS"
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
                mot2_parser[1]="I-PERS"
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
                mot3_parser[1]="I-PERS"
        elif "LOCATION" in line:  
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            mot1_parser[1]="B-LOC"
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
                mot2_parser[1]="I-LOC"
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
                mot3_parser[1]="I-LOC"
        elif "DATE" in line or "TIME" in line or "MONEY" in line or "PERCENT" in line or "FACILITY" in line or "GPE" in line:
            line_parser = line.split(" ")
            mot1_parser = line_parser[1].split("/")
            mot1_parser[1]="B-MISC"
            if len(line_parser) > 2:
                mot2_parser = line_parser[2].split("/")
                mot2_parser[1]="I-MISC"
            if len(line_parser) > 3:
                mot3_parser = line_parser[3].split("/")
                mot3_parser[1]="I-MISC"
        else:
            line_parser = line.split("/")
            mot1_parser[0]=line_parser[0]
            mot1_parser[1]="O"
        outFile.write(mot1_parser[0]+"\t"+mot1_parser[1]+"\n")
        print(mot1_parser[0]+"/"+mot1_parser[1])
        if mot2_parser[1] != "":
            outFile.write(mot2_parser[0]+"\t"+mot2_parser[1]+"\n")
            print(mot2_parser[0]+"/"+mot2_parser[1])
        if mot3_parser[1] != "":
            outFilePos.write(mot3_parser[0]+"\t"+mot3_parser[1]+"\n")
            print(mot3_parser[0]+"/"+mot3_parser[1])
    fp.close()
    outFile.close()

named_entities(words_named)





inFile.close()
