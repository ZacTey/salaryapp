import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('modelSEExtraTree.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input1 = request.form.get("job_title")
    input2 = request.form.get('exp')
    input3 = request.form.get('level')
    input4 = request.form.get('industry')
    input5 = request.form.get('Job Description')
    int_features = list(input2) + list(input3) + list(input4) 
    final_features = pd.DataFrame(int_features)
    final_features = final_features.transpose()
    prediction = model.predict(final_features)
    output = prediction[0]
    return render_template('index.html', prediction_text='Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
