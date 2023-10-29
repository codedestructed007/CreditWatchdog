import sys
sys.path.append(r"C:\Users\Dell\OneDrive\Desktop\Real_projects\Credit_Card_Fraud_Detection")
from src.mlproject import logger
from src.mlproject.config.configuration import  ConfigurationManager
from src.mlproject.components.data_transformation import DataTransformation


STAGE_NAME = 'Data Transformation Stage'

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        
        data_transformation = DataTransformation(data_transformation_config)
        # feature engineering
        feature_engineered_dataframe = data_transformation.feature_engineering()
        # data encoding
        data_encoded_dataframe =data_transformation.data_encoding(feature_engineered_dataframe)
        # preprocessing
        preprocessed_dataframe = data_transformation.preprocess_before_training(data_encoded_dataframe)
        # data splitting
        data_transformation.train_test_split(preprocessed_dataframe)
        


if __name__ == '__main__':
    try:
        logger.info('>>>>>Stage {} started'.format(STAGE_NAME))
        obj = DataTransformationPipeline()
        obj.main()
        logger.info('>>>>>>Stage {} completed'.format(STAGE_NAME))
    except Exception as e:
        logger.exception(e)
        raise e

