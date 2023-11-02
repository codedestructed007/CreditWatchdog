import pandas as pd
import numpy as np
import joblib
import pytest
from pathlib import Path

X_train_path = 'artifacts/data_transformation/X_train.csv'
X_test_path = 'artifacts/data_transformation/X_test.csv'
model_path = Path('artifacts/model_trainer/model.joblib')
y_test_path = 'artifacts/data_transformation/y_test.csv'
male_sample = [3423,24,0,2,2,1,-1,-2, 4223,523,1,0,1,0,0,0,1,0,0]
female_sample = [3423,24,0,2,2,1,-1,-2, 4223,523,0,1,1,0,0,0,1,0,0]
# Define functions as fixtures
@pytest.fixture
def data_leak():
    X_train = pd.read_csv(X_train_path)
    X_test = pd.read_csv(X_test_path)
    
    X = pd.concat([X_train, X_test])
    assert X.shape[0] == X_train.shape[0] + X_test.shape[0]

@pytest.fixture
def prediction_output_shape():
    ada_model = joblib.load(model_path)
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path)
    prediction = ada_model.predict(X_test)
    assert prediction.shape[0] == y_test.shape[0]

@pytest.fixture
def post_train_scrip():
    ada_model = joblib.load(model_path)
    print('Test for model ' + str(ada_model.__class__.__name__))
    prediction_female_input = ada_model.predict(np.array(female_sample).reshape(1, -1))
    prediction_male_input = ada_model.predict(np.array(male_sample).reshape(1, -1))
    assert prediction_female_input == prediction_male_input



def test_data_leak(data_leak):
    X_train = pd.read_csv(X_train_path)
    X_test = pd.read_csv(X_test_path)
    X = pd.concat([X_train, X_test])
    assert X.shape[0] == X_train.shape[0] + X_test.shape[0]
    

def test_prediction_output_shape(prediction_output_shape):
    ada_model = joblib.load(model_path)
    y_test  = pd.read_csv(y_test_path)
    X_test = pd.read_csv(X_test_path)
    prediction = ada_model.predict(X_test)
    assert prediction.shape[0] == y_test.shape[0]

def test_post_train_script(post_train_scrip):
    ada_model = joblib.load(model_path)
    prediction_female_input = ada_model.predict(np.array(female_sample).reshape(1, -1))
    prediction_male_input = ada_model.predict(np.array(male_sample).reshape(1, -1))
    assert prediction_female_input == prediction_male_input
