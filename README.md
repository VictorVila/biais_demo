# Biais démo

Cette application a été conçue pour servir de support pour expliquer aux élèves de droit ce que c'est que le biais dû aux données d'entraintement.

Live : https://huggingface.co/spaces/VictorVS/biais_demo 

## Scénario

Une entreprise veut fluidifier son processus de recrutement et lance un projet d'IA qui trie des CVs. Cette IA est entraînée avec l'historique d'entretiens de recrutement ménés dans la entreprise et les données utilisées. Chaque entretien est représenté comme une ligne d'un tableau qui précise des informations des candidats ansi que l'issue de l'entretien. 

Imaginons qu'un recrutement est lancé pour embaucher un profil "confirmé".

## L'application

Aux fins de l'exercice, les données proposées initialement présentent un biais évident : aucune femme n'a été retenue et tous les hommes ont été recrutés.  

En cliquant sur le bouton "soumettre", l'application va entraîner un premier modèle à partir des données biaisées, puis elle l'applique à la liste de CVs en attente et propose des prédictions sur le recrutement ou pas de la personne. Une deuxième tableau présente l'importance des diffférentes caractéristiques en fonction des recrutements historiques.

Essayez à changer le tableau de données pour que l'application apprenne à détecter les profils "confirmés".

 