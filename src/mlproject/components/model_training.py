import os
from src.mlproject import logger
import joblib


import pandas as pd
from sklearn.ensemble import AdaBoostClassifier

from src.mlproject.entity.config_entity import ModelTrainingConfig



class ModelTrainer:
    def __init__(self, config : ModelTrainingConfig) -> None:
        self.config = config
    
    def train(self):
        X_train = pd.read_csv(self.config.train_input_data_path)
        X_test = pd.read_csv(self.config.test_input_data_path)
        y_train = pd.read_csv(self.config.train_output_data_path)
        y_test = pd.read_csv(self.config.test_output_data_path)
        
        best_params = self.config.parameters
        adc = AdaBoostClassifier(**best_params)
        
        adc.fit(X_train,y_train)
        logger.info('Model Training successfull')
        
        file_path = os.path.join(self.config.root_dir,self.config.model)
        
        joblib.dump(adc,file_path)
    