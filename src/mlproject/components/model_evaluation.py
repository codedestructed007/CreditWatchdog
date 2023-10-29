import joblib
import pandas as pd
from src.mlproject import logger
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,r2_score,classification_report,confusion_matrix,mean_squared_error
from src.mlproject.entity.config_entity import ModelEvaluationconfig

class ModelEvaluation:
    
    def __init__(self,config : ModelEvaluationconfig) -> None:
        self.config = config
    
    
    def Evaluation(self):
        X_test = pd.read_csv(self.config.test_input_data)
        y_test = pd.read_csv(self.config.test_output_data)
        
        #model
        model = joblib.load(self.config.model_dir)
        
        # prediction 
        prediction = model.predict(X_test)
        # accuray
        accuracy = accuracy_score(y_test,prediction)
        
        # Rsquare
        r_square_result = r2_score(y_test,prediction)
        
        # classification report
        report = classification_report(y_test,prediction)
        
        # confusion matrics
        metric = confusion_matrix(y_test,prediction)
        
        model_evaluation_score = [accuracy,r_square_result,report,metric]
        model_evaluation_name = ['Accuracy','R_square','Classification Report','Confusion Matrix']
        
        for i in range(len(model_evaluation_score)):
            with open(self.config.metric_file_name, 'a') as f:
                f.write('{} - {}\n'.format(model_evaluation_name[i],model_evaluation_score[i]))