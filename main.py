import sys
sys.path.append(r"C:\Users\Dell\OneDrive\Desktop\Real_projects\Credit_Card_Fraud_Detection")
from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_datatransformation import DataTransformationPipeline
from src.mlproject.pipeline.stage_04_model_training import ModelTrainingPipeline
from src.mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = 'Data Ingestion'
try:
    logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation'
try:
    logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation'

try:
    logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
    obj = DataTransformationPipeline()
    obj.main()
    logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training'
try:
    logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation'
try:
    logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e