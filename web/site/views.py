from core.db_access import MyDb
from . import app
from flask import render_template


@app.route('/')
def home():
    db = MyDb("/app/data")
    return "Home is coming soon!"


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


def get_best_price_ever(db):
    best_price_ever = db.execute_query("""SELECT min(price/size) as minprice from price_history""")
    return best_price_ever[0][0]


@app.route("/buy-now")
def buy_now():
    db = MyDb("/app/data")
    all_time_low = get_best_price_ever(db)
    current_prices = db.execute_query("""SELECT "date", name, price, size, price_history.url, price/size as pertera from price_history 
inner join (
SELECT url, max("date") as latest_date from price_history group by url
) ld
where "date"=ld.latest_date and ld.url = price_history.url""", keys=("date", "name", "price", "size", "url", "pertera"))
    best_deal = min(current_prices, lambda cp: cp["pertera"])
    return render_template("current_lowest.html", link=best_deal["url"], name=best_deal["name"],
                           price=best_deal["price"], pertera=best_deal["pertera"],
                           diff_from_best=best_deal["pertera"] - all_time_low)
