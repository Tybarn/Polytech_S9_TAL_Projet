# Polytech ET5 Info : TAL : Projet

Projet réalisé dans le cadre du cours de TAL en ET5 Info au sein de Polytech Paris-Saclay.

Groupe : Théo LEGRAS, Alexis PROUST et Jordane MINET

Le but principal de ce projet est d'installer et évaluer sur leurs performances, points forts et faiblesses, différentes plateformes open source d'analyse linguistique.<br/>
Vous pourrez ici étudier 3 plateformes : Stanford Core NLP, CEA List LIMA et NLTK.
Le projet se structure autour de 2 exercices :
	- Exo 1 : Evaluation de l'analyse morpho-syntaxique
	- Exo 2 : Evalution de la reconnaissance d'entités nommées

## Installation

CONDITIONS PREALABLES :
Ne fonctionne que sous Linux (conseillé Ubuntu 16.04 LTS)
Il est nécessaire d'avoir installé au préalable sur votre machine :
	- Java (JRE, JDK, version 1.8 minimum conseillée)
	- Python (version 3.5 et 2.7.12+)
Stanford est fourni dans ce dépôt git.
Pour LIMA : 
	- ```sudo apt-get install qt5-default libqt5xmlpatterns5 libqt5quick5 libqt5declarative5 libboost-all-dev libenchant1c2a libtre5```
	- Svmtool ++ ```sudo dpkg -i svmtool-cpp-1.1.7-ubuntu16.deb```
	- Qhttpserver ```sudo dpkg -i qhttpserver-0.0.1-ubuntu16.04.deb```
	- LIMA ```sudo dpkg -i lima-2.1.202001241207530100-9e12819-Ubuntu16.04-x86_64.deb```
Pour NLTK :
	- NTLK : ```pip install --user -U nltk```
	- Numpy : ```pip install --user -U numpy```

INSTALLATION :
Cloner ce dépôt sur votre machine.

## Usage

Le projet est structuré de la manière suivante :
	- src : Contient les scripts python et .sh.
	- data : Contient les fichiers de données manipulées et résultats par exercice.
	- doc : Contient le rapport au format pdf du projet.
	- tp : Les précédents TPs réalisés dans le cadre du cours de TAL.
	
Des scripts .sh ont été créés pour chaque exercice du projet et se situent dans le dossier "src".
Pour lancer l'exercice 1, exécuter le script exo1.sh : ```./exo1.sh``` depuis le dossier "src".
Pour lancer l'exercice 2, exécuter le script exo2.sh : ```./exo2.sh``` depuis le dossier "src".

## Credits

Théo LEGRAS
Alexis PROUST
Jordane MINET

## Sources

[Stanford Core NLP](https://nlp.stanford.edu/software/tagger.shtml)
[CEA List LIMA](https://github.com/aymara/lima)
[NLTK](https://www.nltk.org/)
