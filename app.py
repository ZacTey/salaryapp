import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input1 = request.form.get("job_title")
    input2 = request.form.get('location')
    input3 = request.form.get('level')
    input4 = request.form.get('type')
    input5 = request.form.get('exp')


    return render_template('index.html', prediction_text='Salary should be $ {}'.format(input1))


if __name__ == "__main__":
    app.run(debug=True)
