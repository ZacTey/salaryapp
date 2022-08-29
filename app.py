from flask import Flask, render_template, request, redirect, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import simplejson
import requests
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def view_method():
    dropdown_list = ['Air', 'Land', 'Sea']
    return render_template('index.html', dropdown_list=dropdown_list)

if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(debug=False)
