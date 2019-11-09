from . import app
from flask import render_template


@app.route('/')
def home():
    return "hello world!"


@app.route('/simple')
def aaaa():
    return u"AMAZING !!! 🤷"


@app.route('/template')
def template():
    return render_template('home.html')
