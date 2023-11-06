import os

import sqlite3
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

#lookup(symbol: stock_symbol) -> dict(name: company name, price: float, symbol: stock's symbol capitalised)
from helpers import apology, login_required
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import threading
import sys


# Configure flask application
app = Flask(__name__)

# Configure the database URI (replace 'sqlite:///dudo.db' with your database URI)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dudo.db"

db = SQLAlchemy(app)
#db.create_all()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash = db.Column(db.String(256), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    # Add other fields as needed

# Configure session to use filesystem (instead of signed cookies)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


"""
@app.route("/test")
def test_page():

    db = sqlite3.connect("dudo.db")

    username = 'cris'
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?;", (username,))
    user_record = cursor.fetchall()
    cursor.close()
    db.close()

    user = user_record[0][1]
    return render_template("test.html", test=user)
"""
    
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #show stocks owned, number of shares owned, current price, total value
    username = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]['username']
    cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]['cash']
    shares_owned = db.execute("SELECT symbol, SUM(shares) as shares FROM purchases where username = ? GROUP BY symbol HAVING shares > 0;", username)
    #shares_owned is something like [{'symbol': 'share_symbol1', 'shares': sum_of_shares_1}, {'symbol': 'share_symbol2', 'shares': sum_of_shares_2}]

    #prepare a line for each stock owned
    cash_in_stocks = 0
    for i in range(len(shares_owned)):
        share = shares_owned[i]
        symbol = share['symbol']
        curr_price = lookup(symbol)['price']
        shares_owned[i]['price'] = curr_price #remember that lookup returns a dict in the form of {"name": symbol, "price": price, "symbol":symbol}
        shares_owned[i]['total'] = curr_price * share['shares']
        cash_in_stocks += shares_owned[i]['total']

    #prepare totals line
    stock_totals = {'cash': cash, 'total':cash+cash_in_stocks}

    return render_template("index.html", shares_data = shares_owned, stock_totals = stock_totals)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 404)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 404)
        
        # Query database for username using a Thread instance and starting the thread to read the username
        user_record = User.query.filter_by(username=request.form.get("username").strip()).add_columns(User.hash).first()

        # Check if a user with the specified username exists
        if user_record is not None:
            # Access the username and hash values
            username = user_record[0].username
            hash_value = user_record[1]
        else:
            return apology("user doesn't exist", 400)

        # Ensure username exists and password is correct
        if not check_password_hash(hash_value, request.form.get("password")):
            return apology("invalid username and/or password", 404)

        # Remember which user has logged in
        session["user_id"] = username

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quoted", methods=["GET", "POST"])
@login_required
def quoted():
    """Get stock quote."""
    return render_template("quoted.html")

#register a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # check if reqached via POST -> a username and password were entered
    if request.method == "POST":
        """validate data for new user"""
        user = request.form.get('username').strip()
        password = request.form.get('password').strip()
        pwd_confirm = request.form.get('confirmation').strip()

        if password == "":
            return apology("Must provide a password", 400)
        if user == "":
            return apology("Must provide username", 400)
        if password != pwd_confirm:
            return apology("Passwords don't match", 400)

       # Check if the username already exists in the database
        user_record = User.query.filter_by(username=user).first()
        if user_record:
            return apology("Username taken, please choose a different one", 400)
        

        # Hash the password and insert the new user into the database
        hashpass = generate_password_hash(password)
        init_score = 100

        new_user = User(username=user, hash=hashpass, score=init_score)
        db.session.add(new_user)
        db.session.commit()
        
        return render_template("login.html")
    
    else:
        return render_template("register.html")
       


#change password of registered user
@app.route("/change_pwd", methods=["GET", "POST"])
@login_required
def change_pwd():
    """Change password"""

    if request.method == "POST":

        #check current password
        curr_pwd_user =  request.form.get('curr_pwd')
        if not check_password_hash(db.execute("SELECT hash FROM users WHERE id = ?;", session["user_id"])[0]['hash'], curr_pwd_user):
            return apology("Wrong current password")

        new_pwd = request.form.get('new_pwd')

        if new_pwd == curr_pwd_user:
            return apology("New password equal to former")

        #update hash_value with new password
        new_hashpass = generate_password_hash(new_pwd)
        db.execute("UPDATE users SET hash = ? where id = ?;", new_hashpass, session["user_id"])
        return render_template("login.html")

    else:
        user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]['username']
        return render_template("change_pwd.html", user = user)

def write_new_user(user, hashpass):
    init_score = 100
    db = sqlite3.connect("dudo.db")
    try: 
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, hash, score) values(?, ?, ?);", (user, hashpass, init_score))
        db.commit()
    except Exception as e:
        db.rollback()
        return f"Error writting in database"
    else:
        db.close()

def read_user_name(username):
    global query_data
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", username)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    query_data = data


if __name__ == "__main__":
    app.run(debug=True)