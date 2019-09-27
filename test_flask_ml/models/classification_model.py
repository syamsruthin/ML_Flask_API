#All sklearn imports here

import pickle as pkl
from flask import request
import os

class classification_model():
    def __init__(self):
        #Load all the saved models for prediction.Also load if there are any model created for preprocessing        
        model_store_dir = "F:/python_practice/ml_model_flask/test_flask_ml/test_flask_ml/model_store/"
        with open(model_store_dir+"log_reg.pkl",'rb') as f:
            self.model = pkl.load(f)

    def predict(self):
        #Reqeust comes as {"record":[2.3]} [2.3]-> feature vector
        data = request.json["record"]    #Should be handled based on incoming record    		
        predicted_class = self.model.predict([data])        
        resp = {"Predicted Class": str(predicted_class[0])}
        return resp

    #More methods can be written for training/preprocessing the incoming record

        
