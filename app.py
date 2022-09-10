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
    if request.method == 'POST':
        input1 = request.form.get("job_title")
        input2 = request.form.get('location')
        input3 = request.form.get('level')
        input4 = request.form.get('type')
        input5 = request.form.get('exp')
        input6 = request.form.get('jobdes')
        input_all = [input1] + [input2] + [input3] + [input4] + [input5]
        int_features = [input_all]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = prediction[0]
        return output
    return render_template('index.html', prediction_text='Salary should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
