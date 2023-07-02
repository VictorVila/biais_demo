# Biais démo

Cette application a été conçue pour servir de support pour expliquer aux élèves de droit ce que c'est que le biais dû aux données d'entraintement.

## Scénario

Une entreprise veut fluidifier son processus de recrutement et lance un projet d'IA qui trie des CVs. Cette IA est entrainée avec l'historique d'entretiens de recrutement ménés dans la entreprise et les données utilisées. Chaque entretien est représenté comme une ligne d'un tableau qui précise des informations des candidats ansi que l'issue de l'entretien. 

Imaginons qu'un recrutement est lancé pour embaucher un profil "confirmé".

## L'application

Aux fins de l'exercise, les données proposées initialement présentent un biais évident : aucune femme n'a été retenue et tous les hommes ont été recrutés.  

En cliquant sur le bouton "soumettre", l'application va entrainer un premier modèle à partir des données biaisées, puis elle l'applique à la liste de CVs en attente et propose des prédictions sur le recrutement ou pas de la personne. Une deuxième tableau présente l'importance des diffférentes caractéristiques en fonction des recrutements historiques.

Essayez à changer le tableau de données pour qu'il aprenne à détecter les profils "confirmés".





---
title: Biais Demo
emoji: 🏢
colorFrom: yellow
colorTo: blue
sdk: gradio
sdk_version: 3.35.2
app_file: app.py
pinned: false
license: creativeml-openrail-m
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
