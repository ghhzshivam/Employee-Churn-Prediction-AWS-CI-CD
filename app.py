from flask import Flask,request,render_template
import numpy as np
import pandas as pd


from predict_pipline import CustomData, PredictPipeline


application = Flask(__name__)

app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/', methods=['GET','POST'])
def predict_datapoint():
    try:
        if request.method == 'GET':
            return render_template('predict.html')
        
        else:
            data = CustomData(
                Education=request.form.get('Education'),
                City=request.form.get('City'),
                Gender=request.form.get('Gender'),
                EverBenched=request.form.get('EverBenched'),
                JoiningYear=int(request.form.get('JoiningYear')),
                PaymentTier=int(request.form.get('PaymentTier')),
                Age=int(request.form.get('Age')),
                ExperienceInCurrentDomain=int(request.form.get('ExperienceInCurrentDomain')),
            )

            pred_df = data.get_datafame()
            print('Before Prediction')
            pred_pipline = PredictPipeline()
            results = pred_pipline.make_predictions(pred_df)
            print('After prediction')
            res = ''
            if results[0] ==1:
                res = 'Emploee will leave the company'
            else:
                res = 'Emplyoee will not leave the company'
            return render_template('predict.html', results=res)

    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template('predict.html', results = e)

if __name__ == '__main__':
    app.run(debug=True)
