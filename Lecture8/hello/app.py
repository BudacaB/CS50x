import random
from flask import Flask, render_template, request

app = Flask(__name__) # serving this Flask app from this file

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/hello")
def hello():
    name = request.args.get("name")
    if not name:
        return render_template("failure.html")
    return render_template("hello.html", name=name)