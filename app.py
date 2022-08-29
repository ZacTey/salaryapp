from flask import Flask, render_template, request, redirect, jsonify
import simplejson
import requests
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/post_field/", methods=['post'])
def open_url():
    text = request.form['this_form']
    old_url = 'https://hkptbr4goi.execute-api.ap-southeast-1.amazonaws.com/Beer_RecSys/userID/???'
    url = old_url.replace('???', text)
    try:
        uResponse = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    rcmd = data['Items'][0]['recommendation']
    return render_template("index.html", value1=data)
    #return redirect(url)


if __name__ == "__main__":
    app.run(debug=False)
