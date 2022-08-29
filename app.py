from flask import Flask, render_template, request, redirect, jsonify
import simplejson
import requests
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['GET'])
def dropdown():
    colours = ['SBI', 'Kotak', 'Citi', 'AMEX', 'BOB', 'AXIS', 'HDFC', 'IDBI', 'YES', 'IndusInd']
    return render_template('index.html', colours=colours)


@app.route('/dropdown', methods = ['POST'])
def dropp():
    dropdownval = request.form.get('colour')
    print(dropdownval)
    return redirect("/", code=302)
if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(debug=False)
