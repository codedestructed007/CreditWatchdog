import os

from src.mlproject.constants import *
from src.mlproject.utils.common import  read_yaml,create_directories
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig 
from src.mlproject.entity.config_entity import DataTransformationConfig,ModelTrainingConfig,ModelEvaluationconfig
from src.mlproject.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_location = config.source_location,
            local_data_file= config.local_data_file
        )
        return data_ingestion_config

    # data validation configuration:
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            data_dir=config.data_dir,
            all_schema=schema
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_trainer
        params = self.params
        create_directories([config.root_dir])
        
        model_training_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            train_input_data_path=config.train_input_data_path,
            test_input_data_path=config.test_input_data_path,
            train_output_data_path=config.train_output_data_path,
            test_output_data_path=config.test_output_data_path,
            parameters=params.parameters,
            model_name=config.model_name
            
        )
        return model_training_config
    
    def get_model_evaluation_config(self):
        config= self.config.model_evaluation
        
        create_directories([config.root_dir])
        
        model_evaluation_config = ModelEvaluationconfig(
            root_dir=config.root_dir,
            model_dir=config.model_path,
            test_input_data = config.test_input_data_path,
            test_output_data = config.test_ouput_data_path,
            metric_file_name = config.metric_file_name
        )
        return model_evaluation_config