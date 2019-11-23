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


@app.route("/best")
def best():
    db = MyDb("/app/data")
    best_price_ever = db.execute_query("""select url, size, price, name, date, a.minprice from price_history 
inner join (
SELECT min(price/size) as minprice from price_history
) a
where price/size=a.minprice""")
    r = best_price_ever[0]
    url, size, price, name, date, minprice = r
    return render_template("best.html", bestprice=minprice, date=date, link=url, drivename=name)


@app.route('/simple')
def aaaa():
    return u"AMAZING !!! 🤷"


@app.route('/template')
def template():
    return render_template('home.html')
