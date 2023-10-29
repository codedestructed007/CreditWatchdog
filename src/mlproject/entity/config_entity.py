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
    
