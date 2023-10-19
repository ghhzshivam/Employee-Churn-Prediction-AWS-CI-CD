import sys
import numpy as np
import pandas as pd
import pickle

class PredictPipeline:
    def __init__(self):
        pass

    def make_predictions(self, features):
        try:
            print('Loading model')
            model = pickle.load(open('artifacts/emplyeechurn xgb.pkl', 'rb'))
            pred = model.predict(features)
            return pred
        
        except Exception as e:
            print(e)

class CustomData:
    def __init__(self, 
            Education : str,
            JoiningYear : int,
            City :str,
            PaymentTier : int,
            Age : int,
            Gender : str,
            EverBenched : str,
            ExperienceInCurrentDomain : int):
        
        self.Education =Education
        self.JoiningYear =JoiningYear
        self.City =City
        self.PaymentTier = PaymentTier
        self.Age =Age
        self.Gender =Gender
        self.EverBenched =EverBenched
        self.ExperienceInCurrentDomain =ExperienceInCurrentDomain

    def get_datafame(self):
        try:
            custom_data_dict = {
                'Education': self.Education,
                'JoiningYear': self.JoiningYear,
                'City': self.City,
                'PaymentTier': self.PaymentTier,
                'Age': self.Age,
                'Gender': self.Gender,
                'EverBenched': self.EverBenched,
                'ExperienceInCurrentDomain': self.ExperienceInCurrentDomain
            }

            x = pd.DataFrame([custom_data_dict])

            num = x.select_dtypes(exclude = 'object')
            char = x.select_dtypes(include = 'object')
            
            # importing one ot encoding
            ohe = pickle.load(open('artifacts/ohe.pkl', 'rb'))

            char_ohe = ohe.transform(char).toarray()
            ohe_fe = pd.DataFrame(char_ohe)
            ohe_fe.columns = [f'Column_{i+1}' for i in range(ohe_fe.shape[1])]

            print(ohe_fe)
            main_df = pd.concat([num, ohe_fe], axis = 1)

            return main_df
        
        except Exception as e:
            print(e)

    def __str__(self):
        return str({
                'Education': self.Education,
                'JoiningYear': self.JoiningYear,
                'City': self.City,
                'PaymentTier': self.PaymentTier,
                'Age': self.Age,
                'Gender': self.Gender,
                'EverBenched': self.EverBenched,
                'ExperienceInCurrentDomain': self.ExperienceInCurrentDomain
            }
)