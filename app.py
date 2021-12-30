# pip freeze > requirements.txt export library to file txt
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
