# Biais démo

Application de support pour expliquer aux élèves de droit ce que c'est que le biais dû aux données d'entraînement.

Live : https://huggingface.co/spaces/VictorVS/biais_demo 

## Scénario

Une entreprise veut fluidifier son processus de recrutement et lance un projet d'IA qui **trie des CVs**. Pour cela, l'IA est entraînée avec les données issues des entretiens de recrutement précédents. L'idée subjacente est que l'IA sera capable de découvrir les critères de sélection partagés par les CV des personnes recrutées. Concrètement, chaque entretien est représenté comme une ligne d'un tableau qui comporte des informations des candidats ainsi que l'issue de l'entretien. 

Imaginons qu'un recrutement est lancé pour embaucher un profil "confirmé" et que les données d'entraînement présentent un biais évident : aucune femme n'a été retenue et tous les hommes ont été recrutés sans tenir compte de leur profil (junior, confirmé ou senior). L'IA saura-t-elle préconiser les profils confirmés ? 

Pour le savoir il suffit de cliquer sur le bouton "soumettre" qui lance ces actions :

1. Entraînement d'un modèle à partir de données fournies ;
2. Utilisation du modèle pour réaliser des prédictions sur des données de test ;
3. Calcul et affichage de l'importance accordée par le modèle à chaque colonne des données ;

Les résultats sont ceux que vous attendiez ? 

Sauriez-vous modifier les données d'entraînement pour éviter le biais et qu'il réussisse à identifier les profils "confirmés" ? Essayez à le faire et cliquez à nouveau sur "Soumettre".  

 
