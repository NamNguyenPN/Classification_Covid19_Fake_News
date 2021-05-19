import pandas as pd
import numpy as np
import pickle, load_dataset
from sklearn.metrics import precision_score,recall_score,f1_score,accuracy_score

_MODEL_PATH="./model/"
_PREPROCESS_PATH="./preprocess/"

_MODEL_FILENAME="SVC.sav"
_PREPROCESS_FILENAME="tfidf.pickle"

_MODEL=_MODEL_PATH+_MODEL_FILENAME
_PREPROCESS=_PREPROCESS_PATH+_PREPROCESS_FILENAME

##### Load model and preprocess ####

_model=pickle.load(open(_MODEL,'rb'))
_tf_idf=pickle.load(open(_PREPROCESS,'rb'))

####################################
### preprocess def ###
def preprocess(sentence):
    list_sentences=np.array([])
    list_sentences=np.append(list_sentences,sentence)
    return _tf_idf.transform(list_sentences)

### Test model ###
def test_model():
    df_perf_metrics = pd.DataFrame(columns=[
    'Model', 'Accuracy_Test_Set', 'Precision',
    'Recall', 'f1_score',
])
    X_train,X_test,y_train,y_test=load_dataset.load()
    X_test=preprocess(X_test)
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
def clasify(sentence):
    label=_model.predict(preprocess(sentence))
    prediction = load_dataset.variety_mappings[label[0]] # Retrieve from dictionary
    # prediction = model.predict(a) # Retrieve from dictionary
    return prediction # Return the predictions
