from src.mlproject.entity.config_entity import DataIngestionConfig
from urllib import request
from src.mlproject import logger
import zipfile
import os
from src.mlproject.utils.common import get_size
from pathlib import Path
import shutil


class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config

    # make sure data is in .csv file and stored in dataset directory
    def transfer_csv_to_new_location(self,source_file = r"C:\Users\Dell\OneDrive\Desktop\Real_projects\Credit_Card_Fraud_Detection\Dataset\UCI_Credit_Card.csv"):
        destination_file = self.config.local_data_file
        if not os.path.exists(self.config.local_data_file):
            shutil.copy(source_file,destination_file)

            logger.info("csv copied from {} to {}:".format(source_file,destination_file))
        else:
            logger.info("file already exists of size : {}".format(get_size(Path(self.config.local_data_file))))



