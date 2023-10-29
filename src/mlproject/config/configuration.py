import os

from src.mlproject.constants import *
from src.mlproject.utils.common import  read_yaml,create_directories
from src.mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig 
# from src.mlproject.entity.config_entity import DataTransformationConfig
from src.mlproject.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.mlproject.entity.config_entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        # self.params = read_yaml(params_filepath)
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