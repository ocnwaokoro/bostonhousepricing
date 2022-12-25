import pickle
import json
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd
import sklearn

app = Flask(__name__)
# Load the model
regmodel = pickle.load(open('regmodel.pkl','rb'))
scalar = pickle.load(open('scaling.pkl','rb'))

# The first route
@app.route('/')
# home page
def home():
    return render_template('home.html')

# create predict api
@app.route('/predict_api',methods=['POST'])

def predict_api():
    # whenever the predict api is pressed, data is given in json format & stored in data
    data = request.json['data']
    print(data)
    # in json it will be in key value pairs so you need to get the values
    # single datapoint record that you get
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    # output is 2-d array
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template('home.html',prediction_text="The House Price Prediction is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)


