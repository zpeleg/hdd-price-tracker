import pathlib
import sqlite3
from pprint import pprint


class MyDb(object):
    def __init__(self, data_dir):
        path = pathlib.Path(data_dir).joinpath("database.db")
        self.db = sqlite3.connect(str(path.absolute()))

    def _table_exists(self, table_name):
        cursor = self.db.cursor()
        cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='{}'""".format(table_name))
        return cursor.fetchall()

    def _create_table(self):
        c = self.db.cursor()
        print("Creating table")
        c.execute("""
              CREATE TABLE price_history
              (id INTEGER PRIMARY KEY ASC, 
              url varchar(500) NOT NULL, 
              size REAL NOT NULL, 
              price REAL NOT NULL,
              name varchar(250) NOT NULL,
              date INT NOT NULL
              )
              """)
        self.db.commit()

    def save_rows(self, rows):
        if not self._table_exists("price_history"):
            self._create_table()
        cursor = self.db.cursor()
        for r in rows:
            cursor.execute("""INSERT INTO price_history(url, size, price, name, date) VALUES(?,?,?,?,?)""",
                           (r["url"], r["size"], r["price"], r["name"], r["date"]))
        self.db.commit()

    def show_all_rows(self):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM price_history""")
        pprint(cursor.fetchall())
