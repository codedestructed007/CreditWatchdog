import time
from flask import Flask, render_template , request, jsonify
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.config.configuration import ConfigurationManager
import pandas as pd
import joblib
from src.mlproject import logger

application = Flask(__name__)

app = application


@app.route('/',methods=['GET'])
def homepage():
    return render_template('home.html')

@app.route('/form',methods=['GET'])
def formpage():
    return render_template('form.html')

@app.route('/future_goals',methods=['GET'])
def futurepage():
    return render_template('future_plans.html')

@app.route('/accuracy',methods= ['GET'])
def accuracyapge():
    return render_template('accuracy.html')


@app.route('/predict',methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        
        try: 
            app.logger.info(request.form.keys()) 
            form_data = {
            "LIMIT_BAL": request.form['limit'],
            "AGE": request.form['age'],
            "code_repayment_sept": request.form['pay_0'],
            "code_repayment_aug": request.form['pay_2'],
            "code_repayment_july": request.form['pay_3'],
            "code_repayment_june": request.form['pay_4'],
            "code_repayment_may": request.form['pay_5'],
            "code_repayment_april": request.form['pay_6'],
            "Dues": request.form['dues'],
            "Previous_payments": request.form['previous_payments'],
            "SEX_1" : request.form['sex_1'],
            "SEX_2" : request.form['sex_2'],
            "EDUCATION_1": request.form['Education_1'],
            "EDUCATION_2" : request.form['Education_2'],
            "EDUCATION_3" : request.form['Education_3'],
            "EDUCATION_4" : request.form['Education_4'],
            "MARRIAGE_1" : request.form['Marriage_1'],
            "MARRIAGE_2" : request.form['Marriage_2'],
            "MARRIAGE_3" : request.form['Marriage_3']
            
        }
        except Exception as e:
            raise e

        # create dataframe with above values
        df_input = pd.DataFrame(form_data,index = [0])
        
     
        try:
            model_path = "artifacts/model_trainer/model.joblib"
            model = joblib.load(model_path)
            
            #prediction
            # response time
            start_time = time.time()
            output = model.predict(df_input)
            end_time = time.time()
            respose_time = end_time - start_time
            respose_time = round(respose_time,2)
            result = int(output[0])

        except Exception as e:
            raise e
        
        return render_template('prediction.html',result = result, time = respose_time)

    return jsonify({'Error': 'invalid request.'})
   


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)