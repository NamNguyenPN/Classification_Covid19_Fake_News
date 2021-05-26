import pickle,load_dataset,sys
import numpy as np
import pandas as pd
from preprocess import text_preprocess
from sklearn.metrics import precision_score,recall_score,f1_score,accuracy_score

print("CALLED")

_MODEL_PATH="./model/"
_PREPROCESS_PATH="./preprocess/"

_MODEL_FILENAME="SVC.sav"
_PREPROCESS_FILENAME="TF_IDF.sav"

_MODEL=_MODEL_PATH+_MODEL_FILENAME
_PREPROCESS=_PREPROCESS_PATH+_PREPROCESS_FILENAME

##### Load model and preprocess ####

_model=pickle.load(open(_MODEL,'rb'))
_tf_idf=pickle.load(open(_PREPROCESS,'rb'))

####################################
### preprocess Function ###
def preprocess(sentence):
    sentence=text_preprocess.contraction(sentence)
    sentence=text_preprocess.tokenize(sentence)    
    sentence=text_preprocess.remove_stopword(sentence)
    return sentence
### Vectorize Function 
def vectorize(sentence):
    if(type(sentence)==str):
        arr=[]
        arr.append(sentence)
        sentence=arr
    return _tf_idf.transform(sentence)
### Test model ###
def test_model():
    df_perf_metrics = pd.DataFrame(columns=[
    'Model', 'Accuracy_Test_Set', 'Precision',
    'Recall', 'f1_score',
])
    train,test=load_dataset.load()
    test["tweet"]=test['tweet'].apply(lambda x:preprocess(x))
    X_test=vectorize(test['tweet'].values)
    y_test=test['label']
    y_pred=_model.predict(X_test)
    df_perf_metrics.loc[1] = [
        type(_model).__name__,
        _model.score(X_test, y_test),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ]
    return print(df_perf_metrics)


### Clasify on Website ###
def classify(sentence):
    label=_model.predict(vectorize(preprocess(sentence)))
    prediction = load_dataset.variety_mappings[label[0]] # Retrieve from dictionary
    # prediction = model.predict(a) # Retrieve from dictionary
    return prediction # Return the predictions
