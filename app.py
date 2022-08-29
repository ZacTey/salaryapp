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
    jobs = ['job1', 'job2', 'job3']
    return render_template('index.html', jobs=jobs)


@app.route('/dropdown', methods = ['POST'])
def dropp():
    dropdownval = request.form.get('job')
    print(dropdownval)
    return redirect("/", code=302)
if __name__ == "__main__":
    app.run()



if __name__ == "__main__":
    app.run(debug=False)
