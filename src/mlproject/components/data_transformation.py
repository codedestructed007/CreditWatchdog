from src.mlproject import logger
import os
import pandas as pd
from src.mlproject.entity.config_entity import DataTransformationConfig

# sklearn import
from sklearn.model_selection import train_test_split
    
class DataTransformation:
    def __init__(self, config = DataTransformationConfig) -> None:
        self.config  = config
        
    def feature_engineering(self):
        try:
            df = pd.read_csv(self.config.data_path)
            print(df.columns)
            # Renaming columns name
            df= df.rename(columns={
                'PAY_0' : 'code_repayment_sept',
                'PAY_2' : 'code_repayment_aug',
                'PAY_3' : 'code_repayment_july',
                'PAY_4' : 'code_repayment_june',
                'PAY_5' : 'code_repayment_may',
                'PAY_6' : 'code_repayment_april',
                'BILL_AMT1': 'bill_sept',
                'BILL_AMT2' : 'bill_aug',
                'BILL_AMT3' : 'bill_july',
                'BILL_AMT4' : 'bill_june',
                'BILL_AMT5' : 'bill_may',
                'BILL_AMT6': 'bill_april',
                'PAY_AMT1' : 'previous_payment_sept',
                'PAY_AMT2' : 'previous_payment_aug',
                'PAY_AMT3' : 'previous_payment_july',
                'PAY_AMT4' : 'previous_payment_june',
                'PAY_AMT5' : 'previous_payment_may',
                'PAY_AMT6' : 'previous_payment_april',
                'default.payment.next.month' : 'will_default'
})          
            #replacing some educations values to a valid category
            
            df['EDUCATION'].replace({
                0 : 4, 5 : 4, 6: 4
            },inplace=True)
            
            df['MARRIAGE'].replace({
                0 : 3
            }, inplace=True)
            
            df['Dues'] = df['bill_sept'] + df['bill_aug'] + df['bill_july']+ df['bill_june'] + df['bill_may'] + df['bill_april']
            df['Previous_payments'] = df['previous_payment_april'] + df['previous_payment_aug']+df['previous_payment_july'] + df['previous_payment_june']+df['previous_payment_may'] + df['previous_payment_sept']
            return df
        except Exception as e:
            raise e
        
    def data_encoding(self,df_fe):
        # feature engineered dataset
        try:            
            df_fe = pd.get_dummies(df_fe, columns=['SEX','EDUCATION','MARRIAGE'], dtype=int)
            logger.info('OnehotEncoding performed sucessfully')
            
            return df_fe
        except Exception as e:
            raise e
    
    def preprocess_before_training(self,df_encoded):
        try:
            df_encoded.drop(['ID','bill_sept','bill_aug','bill_july','bill_june','bill_may','bill_april','previous_payment_sept','previous_payment_aug','previous_payment_july','previous_payment_may','previous_payment_june','previous_payment_april'],axis=1, inplace=True)
            logger.info('Final Preprocessing sucessfully completed')
            
            return df_encoded
        except Exception as e:
            raise e
        
    def train_test_split(self,df_preprocessed) -> None:
        try:
            X = df_preprocessed.drop(['will_default'],axis=1)
            y = df_preprocessed[['will_default']]
            X_train,X_test, y_train,y_test = train_test_split(X,y, random_state=42)
            logger.info('Train-Test splitting successfull')
            
            X_train.to_csv(os.path.join(self.config.root_dir, 'X_train.csv'),index=False)
            X_test.to_csv(os.path.join(self.config.root_dir,'X_test.csv'),index = False)
            y_train.to_csv(os.path.join(self.config.root_dir,'y_train.csv'),index=False)
            y_test.to_csv(os.path.join(self.config.root_dir,'y_test.csv'),index=False)
            logger.info('Splitted data loaded to {}'.format(self.config.root_dir))
            
        except Exception as e:
            raise e
        

        
    
        
  
        