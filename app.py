# Imports

import pandas as pd
import sklearn
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.compose import ColumnTransformer, make_column_selector as selector
from sklearn.preprocessing import OneHotEncoder   
from sklearn.pipeline import make_pipeline 
import gradio as gr


# Presentation for Huggingface

description = "Simple app for demonstration of data bias"
title = "Bias demo" 


# App

def get_data_raw() :
    """Returns the initial (and higly biased) train dataset""" 
    data = {
        'Titre' : ['Mme', 'Mme', 'Mme', 'M', 'M', 'M'],
        'Nom' : ['Rachel', 'Phoebe', 'Monica', 'Chandler', 'Joey', 'Ross'],  
        'Expérience' : ['Junior', 'Confirmé', 'Confirmé', 'Junior', 'Senior', 'Confirmé'],
        'Recrutement' : ['Non', 'Non', 'Non', 'Oui', 'Oui', 'Oui'],
    } 
    data_raw = pd.DataFrame(data=data)
    return data_raw


def get_data_test() :
    """Returns the test dataset""" 
    data_test = {
        'Titre' : ['Mme', 'Mme', 'Mme', 'M', 'M', 'M'],
        'Nom' : ['Leia', 'Padme', 'Rei', 'Han Solo', 'Luke', 'Chewbacca'],  
        'Expérience' : ['Junior', 'Confirmé', 'Confirmé', 'Junior', 'Senior', 'Confirmé'],
    } 
    df_data_test = pd.DataFrame(data=data_test)
    return df_data_test

def get_model(data, target) : 
    """Trains a decision tree and returns the model and the classifier itself """ 
    categorical_columns_selector = selector(dtype_include=object) 
    categorical_columns = categorical_columns_selector(data) 
    categorical_preprocessor = OneHotEncoder(handle_unknown="ignore")  
    preprocessor = ColumnTransformer([
        ('categorical', categorical_preprocessor, categorical_columns) 
    ])
    decission_tree = DecisionTreeClassifier()
    pipeline = make_pipeline(preprocessor, decission_tree) 
    return pipeline.fit(data, target), decission_tree

def get_features_importance(model, classifier): 
    """Returns the weight of each feature in the classifier""" 
    df1 = pd.DataFrame(data=model[:-1].get_feature_names_out(), columns=['Critère'])
    df2 = pd.DataFrame(data=classifier.feature_importances_, columns=['Importance'])
    df_concat = pd.concat([df1, df2], axis=1)
    return df_concat 

def get_output(data_raw): 
    """Applies the model to the test data and gets predictions.
    Returns the test data along qith the predictions and the importance of each feature"""      
    data = data_raw.drop(columns=['Nom','Recrutement'])
    target = data_raw.Recrutement 
    model, decission_tree = get_model(data, target)  
    data_test = get_data_test() 
    predictions = model.predict(data_test) 
    result = pd.concat([data_test, pd.DataFrame(data = predictions, columns={'Predictions'})], axis = 1)
    features_importance = get_features_importance(model, decission_tree)
    return result, features_importance


# Launching the Gradio UI 

ui = gr.Interface(
    fn=get_output, 
    inputs=[ 
        gr.Dataframe(get_data_raw(), label="Données d'entraînement")
    ],
    outputs=[
        gr.Dataframe(label="Prédictions"),
        gr.Dataframe(label="Importance des paramètres")
    ],
    title="Biais démo",
    description="""Application de support pour expliquer aux élèves de droit ce que c'est que le biais dû aux données d'entraînement.

Live : https://huggingface.co/spaces/VictorVS/biais_demo 

## Scénario

Une entreprise veut fluidifier son processus de recrutement et lance un projet d'IA qui trie des CVs. Pour cela, l'IA est entraînée avec les données issues des entretiens de recrutement précédents. L'idée subjacente est que l'IA sera capable de découvrir les critères de sélection partagés par les CV des personnes recrutées. Concrètement, chaque entretien est représenté comme une ligne d'un tableau qui comporte des informations des candidats ainsi que l'issue de l'entretien. 

Imaginons qu'un recrutement est lancé pour embaucher un profil "confirmé" et que les données d'entraînement présentent un biais évident : aucune femme n'a été retenue et tous les hommes ont été recrutés sans tenir compte de leur profil (junior, confirmé ou senior). L'IA saura-t-elle préconiser les profils confirmés ? 

Pour le savoir il suffit de cliquer sur le bouton "soumettre" qui lance ces actions :

1. Entraînement d'un modèle à partir de données fournies ;
2. Utilisation du modèle pour réaliser des prédictions sur des données de test ;
3. Calcul et affichage de l'importance accordée par le modèle à chaque colonne des données ;

Les résultats sont ceux que vous attendiez ? 

Sauriez-vous modifier les données d'entraînement pour éviter le biais et qu'il réussisse à identifier les profils "confirmés" ? Essayez à le faire et cliquez à nouveau sur "Soumettre".  """)
ui.launch() 