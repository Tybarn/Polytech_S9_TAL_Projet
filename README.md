# Polytech ET5 Info : TAL : Projet

Projet réalisé dans le cadre du cours de TAL en ET5 Info au sein de Polytech Paris-Saclay.

Groupe : Théo LEGRAS, Alexis PROUST et Jordane MINET

Le but principal de ce projet est d'installer et évaluer sur leurs performances, points forts et faiblesses, différentes plateformes open source d'analyse linguistique.<br/>
Vous pourrez ici étudier 3 plateformes : Stanford Core NLP, CEA List LIMA et NLTK.<br/>
Le projet se structure autour de 2 exercices :<br/>
	- Exo 1 : Evaluation de l'analyse morpho-syntaxique<br/>
	- Exo 2 : Evalution de la reconnaissance d'entités nommées

## Installation

CONDITIONS PREALABLES :<br/>
Ne fonctionne que sous Linux (conseillé Ubuntu 16.04 LTS)<br/>
Il est nécessaire d'avoir installé au préalable sur votre machine :<br/>
	- Java (JRE, JDK, version 1.8 minimum conseillée)<br/>
	- Python (version 3.5 et 2.7.12+)<br/>
Stanford est fourni dans ce dépôt git.<br/>
Pour LIMA : <br/>
	- ```sudo apt-get install qt5-default libqt5xmlpatterns5 libqt5quick5 libqt5declarative5 libboost-all-dev libenchant1c2a libtre5```<br/>
	- Svmtool ++ ```sudo dpkg -i svmtool-cpp-1.1.7-ubuntu16.deb```<br/>
	- Qhttpserver ```sudo dpkg -i qhttpserver-0.0.1-ubuntu16.04.deb```<br/>
	- LIMA ```sudo dpkg -i lima-2.1.202001241207530100-9e12819-Ubuntu16.04-x86_64.deb```<br/>
Pour NLTK :<br/>
	- NTLK : ```pip install --user -U nltk```<br/>
	- Numpy : ```pip install --user -U numpy```<br/>

INSTALLATION :<br/>
Cloner ce dépôt sur votre machine.

## Usage

Le projet est structuré de la manière suivante :<br/>
	- src : Contient les scripts python et .sh.<br/>
	- data : Contient les fichiers de données manipulées et résultats par exercice.<br/>
	- doc : Contient le rapport au format pdf du projet.<br/>
	- tp : Les précédents TPs réalisés dans le cadre du cours de TAL.<br/>
	
Des scripts .sh ont été créés pour chaque exercice du projet et se situent dans le dossier "src".<br/>
Pour lancer l'exercice 1, exécuter le script exo1.sh : ```./exo1.sh``` depuis le dossier "src".<br/>
Pour lancer l'exercice 2, exécuter le script exo2.sh : ```./exo2.sh``` depuis le dossier "src".<br/>

## Credits

Théo LEGRAS
Alexis PROUST
Jordane MINET

## Sources

[Stanford Core NLP](https://nlp.stanford.edu/software/tagger.shtml)<br/>
[CEA List LIMA](https://github.com/aymara/lima)<br/>
[NLTK](https://www.nltk.org/)<br/>
