from core.db_access import MyDb
from . import app
from flask import render_template


@app.route('/')
def home():
    db = MyDb("/app/data")
    return str(db.get_all_rows())


@app.route('/table')
def table():
    db = MyDb("/app/data")
    return render_template("home.html", rows=db.get_all_rows())


@app.route('/simple')
def aaaa():
    return u"AMAZING !!! 🤷"


@app.route('/template')
def template():
    return render_template('home.html')
