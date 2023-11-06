import os

#from cs50 import SQL
import sqlite3
from flask import Flask, g, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

#lookup(symbol: stock_symbol) -> dict(name: company name, price: float, symbol: stock's symbol capitalised)

import threading
import sys


# Configure flask application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


class ReadDBThread(threading.Thread):
    def run(self):
        db = sqlite3.connect("dudo.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = 'cris';")
        data = cursor.fetchall()
        cursor.close()
        db.close()
        global x 
        x = data[0]
        session['user'] = 123

        #session["test"] = 'ok' if data and 'username' in data[0] and data[0]['username'] == 'cris' else 'not ok'

@app.route("/")
def test_page():
    
    db = sqlite3.connect("dudo.db")

    username = 'cris'
    cursor = db.cursor()

    #query = "SELECT * FROM users WHERE username = ?;"

    cursor.execute("SELECT * FROM users WHERE username = 'cris';")
    
    user_record = cursor.fetchall()

    username = user_record[0][1]
    cursor.close()
    db.close()



    return render_template("test.html", test=username)



if __name__ == "__main__":
    app.run(debug=True)