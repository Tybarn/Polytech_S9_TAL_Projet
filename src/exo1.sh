#!/bin/bash

echo " --------------------- EXO 1 ---------------------"
# change lima to univ
python python/change_POSTags.py ../data/Exo1/pos_reference.txt.lima ../data/Exo1/pos_reference.txt.lima.tmp ../data/Exo1/POSTags_LIMA_PTB_Linux.txt
python python/change_POSTags.py ../data/Exo1/pos_reference.txt.lima.tmp ../data/Exo1/pos_reference.txt.univ ../data/Exo1/POSTags_PTB_Universal_Linux.txt
rm ../data/Exo1/pos_reference.txt.lima.tmp
echo "Lima -> Univ : Done"
# extract text from univ
python python/extract_text.py ../data/Exo1/pos_reference.txt.univ ../data/Exo1/pos_test.txt
echo "Extract text from Univ : Done"
# work on stanford
cd stanford/stanford-postagger-2018-10-16/
./stanford-postagger.sh models/english-left3words-distsim.tagger ../../data/Exo1/pos_test.txt > ../../data/Exo1/pos_test.txt.pos.stanford
echo "pos_test.txt.pos.stanford : Done"
cd ..
python python/formatage_stanford.py ../data/Exo1/pos_test.txt.pos.stanford ../data/Exo1/POSTags_PTB_Universal_Linux.txt
echo "pos_test.txt.pos.stanford.univ : Done"
python python/evaluate.py ../data/Exo1/pos_test.txt.pos.stanford.univ ../data/Exo1/pos_reference.txt.univ
echo "stanford evaluate : Done"