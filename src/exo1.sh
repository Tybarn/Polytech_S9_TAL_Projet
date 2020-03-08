#!/bin/bash

echo " --------------------- EXO 1 ---------------------"

# extract text from univ
python python/extract_text.py ../data/Exo1/pos_reference.txt.univ ../data/Exo1/pos_test.txt
echo "Extract text from Univ : Done"
### lancement des POS taggers ####
# work on stanford
cd stanford/stanford-postagger-2018-10-16/
./stanford-postagger.sh models/english-left3words-distsim.tagger ../../../data/Exo1/pos_test.txt > ../../../data/Exo1/pos_test.txt.pos.stanford
echo "pos_test.txt.pos.stanford : Done"
cd ../../
python python/format_postags_stanford.py ../data/Exo1/pos_test.txt.pos.stanford ../data/Exo1/POSTags_PTB_Universal_Linux.txt
echo "pos_test.txt.pos.stanford.univ : Done"
python python/normalize.py ../data/Exo1/pos_test.txt.pos.stanford.univ ../data/Exo1/pos_reference.txt.univ
echo "stanford normalisation : Done"
# work on lima
cd ../data/Exo1/
analyzeText -l eng -p main pos_test.txt > pos_test.txt.pos.tmp
python ../../src/python/formatage_lima.py pos_test.txt.pos.tmp
rm pos_test.txt.pos.tmp
echo "pos_test.txt.pos.lima : Done"
cd ../../src
python python/change_POSTags.py ../data/Exo1/pos_test.txt.pos.lima ../data/Exo1/pos_test.txt.pos.lima.tmp ../data/Exo1/POSTags_LIMA_PTB_Linux.txt
python python/change_POSTags.py ../data/Exo1/pos_test.txt.pos.lima.tmp ../data/Exo1/pos_test.txt.pos.lima.univ ../data/Exo1/POSTags_PTB_Universal_Linux.txt
rm ../data/Exo1/pos_test.txt.pos.lima.tmp
python python/normalisationLima.py ../data/Exo1/pos_test.txt.pos.lima.univ
echo "Lima -> Univ : Done"
# evaluate
echo "##################### EVALUATE #####################"
echo "STANFORD :"
python python/evaluate.py ../data/Exo1/pos_test.txt.pos.stanford.univ ../data/Exo1/pos_reference.txt.univ
echo "LIMA :"
python python/evaluate.py ../data/Exo1/pos_test.txt.pos.lima.univ.test ../data/Exo1/pos_reference.txt.univ