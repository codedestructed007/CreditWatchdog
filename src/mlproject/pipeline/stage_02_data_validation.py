import os
from src.mlproject import logger
from src.mlproject.config.configuration import  ConfigurationManager
from src.mlproject.components.data_validation import  DataValidation

STAGE_NAME = 'Data Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        
        data_ingestion = DataValidation(data_ingestion_config)
        data_ingestion.validate_all_columns


if __name__ == '__main__':
    try:
        logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
    except Exception as e:
        logger.exception(e)
        raise e

