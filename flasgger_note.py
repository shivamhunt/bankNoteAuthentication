#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:28:04 2021

@author: hunter
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask  import Flask,request

import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger


app= Flask(__name__)
Swagger(app)
pickel_in=open("cf.pkl","rb")
cf= pickle.load(pickel_in)
@app.route('/')
def Welcome():
  return "welcome all"

@app.route('/predict',methods=["GET"])
def predict_note_authentication():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance =request.args.get('variance')
    skewness =request.args.get('skewness')
    curtosis =request.args.get('curtosis')
    entropy =request.args.get('entropy')
    prediction= cf.predict([[variance,skewness,curtosis,entropy]])
    return str(prediction)




if __name__ == '__main__':
  
  app.run()