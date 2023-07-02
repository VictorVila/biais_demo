import pandas as pd

import sklearn
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.compose import ColumnTransformer, make_column_selector as selector
from sklearn.preprocessing import OneHotEncoder   
from sklearn.pipeline import make_pipeline 
import gradio as gr



description = "Démo simple des biais"
title = "Biais démo"
examples = [["TODO."]]


def get_data_raw() :
    data = {
        'Titre' : ['Mme', 'Mme', 'Mme', 'M', 'M', 'M'],
        'Nom' : ['Rachel', 'Phoebe', 'Monica', 'HChandler', 'Joey', 'Ross'],  
        'Expérience' : ['Junior', 'Confirmé', 'Confirmé', 'Junior', 'Senior', 'Confirmé'],
        'Recrutement' : ['Non', 'Non', 'Non', 'Oui', 'Oui', 'Oui'],
    } 
    data_raw = pd.DataFrame(data=data)
    return data_raw


def get_data_test() :
    data_test = {
        'Titre' : ['Mme', 'Mme', 'Mme', 'M', 'M', 'M'],
        'Nom' : ['Leia', 'Padme', 'Rei', 'Han Solo', 'Luke', 'Chewbacca'],  
        'Expérience' : ['Junior', 'Confirmé', 'Confirmé', 'Junior', 'Senior', 'Confirmé'],
    } 
    df_data_test = pd.DataFrame(data=data_test)
    return df_data_test

def get_model(data, target) : 
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
    df1 = pd.DataFrame(data=model[:-1].get_feature_names_out(), columns=['Critère'])
    df2 = pd.DataFrame(data=classifier.feature_importances_, columns=['Importance'])
    df_concat = pd.concat([df1, df2], axis=1)
    return df_concat 

def get_output(data_raw):
    
    # Le nom n'est pas utile 
    data = data_raw.drop(columns=['Nom','Recrutement'])
    target = data_raw.Recrutement
    
    model, decission_tree = get_model(data, target) 
    
    data_test = get_data_test()
    
    predictions = model.predict(data_test)
    
    result = pd.concat([data_test, pd.DataFrame(data = predictions, columns={'Predictions'})], axis = 1)
    
    features_importance = get_features_importance(model, decission_tree)
    
    return result, features_importance


ui = gr.Interface(
    fn=get_output, 
    inputs=[
        gr.Dataframe(get_data_raw())
    ],
    outputs=[
        gr.Dataframe(),
        gr.Dataframe()
    ],
    description="Show and editable dataframe and use it as output "
)

ui.launch() 