import sys
sys.path.append(r"C:\Users\Dell\OneDrive\Desktop\Real_projects\Credit_Card_Fraud_Detection")
import os
from src.mlproject import logger
from src.mlproject.config.configuration import  ConfigurationManager
from src.mlproject.components.model_evaluation import ModelEvaluation


STAGE_NAME = 'Model evaluation Stage'

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.Evaluation()


if __name__ == '__main__':
    try:
        logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
    except Exception as e:
        logger.exception(e)
        raise e

