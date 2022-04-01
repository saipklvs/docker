import imp
import json
from multiprocessing.spawn import import_main_path
import os 
import numpy as np
import pandas as pd
from joblib import load
from sklearn import preprocessing
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier


from flask import Flask
# Set environnment variables
MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE_LDA = os.environ["MODEL_FILE_LDA"]
MODEL_FILE_NN = os.environ["MODEL_FILE_NN"]
MODEL_PATH_LDA = os.path.join(MODEL_DIR, MODEL_FILE_LDA)
MODEL_PATH_NN = os.path.join(MODEL_DIR, MODEL_FILE_NN)

# Loading the LDA model 
print(f"Loading model from {MODEL_PATH_LDA}")
inference_lda = load(MODEL_PATH_LDA)

# Loading NN model 
print(f"Loading model from {MODEL_PATH_NN}")
inference_NN = load(MODEL_PATH_NN)

# Creation of Flask app
app = Flask(__name__)

# Flask route so that we can server HTTP traffic on that route
@app.route('/line/<Line>')
# Get data from json and return the requested row defined by the variable line
def line(Line):
    with open('./test.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    # We can then find the data for the requested row and send it back as json
    return json.dumps(file_data[Line])

# Flask route so that we can server HTTP traffic on that route
    
