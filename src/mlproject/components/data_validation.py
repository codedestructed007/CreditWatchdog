import pandas as pd
from src.mlproject.config.configuration import DataValidationConfig
from src.mlproject import logger


class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try :
            validation_status = None
            
            data = pd.read_csv(self.config.data_dir)
            all_cols = list(data.columns)
            dtypes = data.dtypes
            
            # all_schema = self.config.all_schema.keys()
            schema_cols = list(self.config.all_schema.keys())
            schema_dtypes = list(self.config.all_schema.values())

            # for col, dtypes in zip(all_cols, dtypes):
            #     if col not in all_schema or (dtypes ):
            #         validation_status = False
            #         with open(self.config.STATUS_FILE, "w") as f:
            #             f.write('Validation status : {}'.format(validation_status))
                        
            for col, schema_col, dtype , schema_dtype in zip(all_cols,schema_cols,dtypes,schema_dtypes):
                if (col != schema_col) or (dtype != schema_dtype):
                    logger.info('Check in feature {} and its data type {}'.format(col,dtype))
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write('VALIDATION STATUS : {}'.format(validation_status)) 
                    return validation_status
                        
        
            validation_status = True
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write("Validation status : {}".format(validation_status))            
                        
            return validation_status
        
        except Exception as e:
            raise e