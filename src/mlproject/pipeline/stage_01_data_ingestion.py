import sys
# to tell the environment from where to import modules
sys.path.append(r"C:\Users\Dell\OneDrive\Desktop\Real_projects\Credit_Card_Fraud_Detection")


import os
from src.mlproject.config.configuration import  ConfigurationManager
from src.mlproject.components.data_ingestion import  DataIngestion
from src.mlproject import logger



STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.transfer_csv_to_new_location()


if __name__ == '__main__':
    try:
        logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
    except Exception as e:
        logger.exception(e)
        raise e