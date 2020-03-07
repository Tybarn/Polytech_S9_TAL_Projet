#!/bin/bash

echo " --------------------- EXO 1 ---------------------"
# change lima to univ
python change_POS.py ../../data/Exo1/pos_reference.txt.lima ../../data/Exo1/pos_reference.txt.lima.tmp ../../data/Exo1/POSTags_LIMA_PTB_Linux.txt
python change_POS.py ../../data/Exo1/pos_reference.txt.lima.tmp ../../data/Exo1/pos_reference.txt.univ ../../data/Exo1/POSTags_PTB_Universal_Linux.txt
echo "Lima -> Univ : Done"
# extract text from univ
python extract_text.py ../../data/Exo1/pos_reference.txt.univ ../../data/Exo1/pos_test.txt
echo "Extract text from Univ : Done"