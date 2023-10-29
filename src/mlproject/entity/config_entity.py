from dataclasses import dataclass
from pathlib import Path

# data ingestion dataclass
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir  : Path
    source_location : str
    local_data_file : Path
    
# data validation dataclass
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE : str
    data_dir : Path
    all_schema : dict
    
# data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    

# Model training
@dataclass(frozen = True)
class ModelTrainingConfig:
    root_dir : Path
    train_input_data_path : Path
    test_input_data_path : Path
    train_output_data_path : Path
    test_output_data_path : Path
    parameters : dict
    model : str
    
    
# Model Evaluation
@dataclass(frozen=True)
class ModelEvaluationconfig:
    root_dir : Path
    model_dir : Path
    test_input_data : Path
    test_output_data : Path
    metric_file_name : Path