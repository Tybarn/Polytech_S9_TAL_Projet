#!/bin/bash

# extract text from univ
python python/extract_text.py ../data/Exo2/ne_reference.txt.conll ../data/Exo2/ne_test.txt
echo "extract ne_test.txt : Done"
# work on Stanford
cd stanford/stanford-ner-2018-10-16
java -mx600m -cp stanford-ner.jar:* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ../../../data/Exo2/ne_test.txt > ../../../data/Exo2/ne_test.txt.ne.stanford
echo "NER Stanford : Done"
cd ../..
python python/format_ner_stanford.py ../data/Exo2/ne_test.txt.ne.stanford ../data/Exo2/NER_STANFORD_CONLL.txt
echo "NER Stanford -> CoNLL : Done"
# evaluate Stanford
python python/evaluate.py ../data/Exo2/ne_test.txt.ne.stanford.conll ../data/Exo2/ne_reference.txt.conll
echo "stanford evaluate : Done"