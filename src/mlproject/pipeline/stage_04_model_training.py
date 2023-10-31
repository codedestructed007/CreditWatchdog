
import os
from src.mlproject import logger
from src.mlproject.config.configuration import  ConfigurationManager
from src.mlproject.components.model_training import ModelTrainer


STAGE_NAME = 'ModeTraining Stage'

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        
        model_training = ModelTrainer(model_training_config)
        model_training.train()


if __name__ == '__main__':
    try:
        logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
    except Exception as e:
        logger.exception(e)
        raise e

