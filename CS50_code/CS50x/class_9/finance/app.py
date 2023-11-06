"""
 C$50 Finance, a web app via which you can manage portfolios of stocks.
 Not only will this tool allow you to check real stocks’ actual prices
 and portfolios’ values, it will also let you buy (okay, “buy”) and sell
 (okay, “sell”) stocks by querying for stocks’ prices.

Indeed, there are tools (one is known as IEX) that let you download
stock quotes via their API (application programming interface) using URLs
like https://api.iex.cloud/v1/data/core/quote/nflx?token=API_KEY.
Notice how Netflix’s symbol (NFLX) is embedded in this URL; that’s
how IEX knows whose data to return. That link won’t actually return
any data because IEX requires you to use an API key, but if it did,
you’d see a response in JSON (JavaScript Object Notation) format.

We’re going to be doing something very similar, with Yahoo Finance.

sqlite3 .schema response to finance.db
CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    username TEXT NOT NULL,
                    hash TEXT NOT NULL,
                    cash NUMERIC NOT NULL DEFAULT 10000.00);
CREATE TABLE sqlite_sequence(name,seq);
CREATE UNIQUE INDEX username ON users (username);
Notice that, by default, new users receive $10,000 in cash

The code comes with 2 @routes already implemented: login and logout

*************************************************************
IMPLEMENTATION:

function register():
Complete the implementation of register in such a way that it allows a
user to register for an account via a form.

Require that a user input a username, implemented as a text field whose name
is username. Render an apology if the user’s input is blank or the username already exists.
Require that a user input a password, implemented as a text field whose name is password,
and then that same password again, implemented as a text field whose name is confirmation.
Render an apology if either input is blank or the passwords do not match.
Submit the user’s input via POST to /register.

INSERT the new user into users, storing a hash of the user’s password, not the password itself.
Hash the user’s password with generate_password_hash Odds are you’ll want to create a new template
(e.g., register.html) that’s quite similar to login.html.

Once you’ve implemented register correctly, you should be able to register for an account and log in
(since login and logout already work)! And you should be able to see your rows via phpLiteAdmin or sqlite3.



"""
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

#lookup(symbol: stock_symbol) -> dict(name: company name, price: float, symbol: stock's symbol capitalised)
from helpers import apology, login_required, lookup, usd
from datetime import datetime



# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get('symbol').strip().upper()

        if symbol == "":
            return apology("must provide a symbol to buy", 403)
        try:
            shares = int(request.form.get('shares'))
        except ValueError:
            return apology("Shares must be a positive integer")
        else:
            if shares <= 0:
                return apology("Shares must be a positive integer")
            else:
                try:
                    #notice that lookup returns a dict in the form of {"name": symbol, "price": price, "symbol":symbol}
                    price_data = lookup(symbol)
                    print(price_data)
                except:
                    return apology("Error retrieving price")
                else:
                    if price_data == None:
                        return apology("Invalid symbol")
                    else:
                        #check if user has enough cash for purchase
                        cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]['cash']
                        print('price:',price_data['price'])
                        print(type(price_data['price']))
                        print('cash:', cash, 'total price:', shares *price_data['price'])
                        if shares * price_data['price'] > cash:
                            return apology("Not enough cash for purchase")
                        else:
                            #make the purchase: 1) create a register in table 'purchases' 2) redude the cash for the user in table 'users 3) return
                            new_cash = cash - shares * price_data['price']
                            user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]['username']
                            db.execute("INSERT INTO purchases (username, symbol, shares, share_price, time_stamp) values(?, ?, ?, ?, ?);", user, symbol, shares, price_data['price'],datetime.now())
                            db.execute("UPDATE users SET cash = ? where id = ?;", new_cash, session["user_id"])
                            return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    #show stocks purchased/sold, number of shares purchased/sold, transaction price, time of transaction
    username = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]['username']
    transactions_data = db.execute("SELECT symbol, shares, share_price, time_stamp FROM purchases where username = ?;", username)
    #remember that transaction will have the form:
    # [{'symbol': 'share_symbol1', 'shares': sum_of_shares_1, 'share_price': price, 'time_stamp': time_stamp}]

    return render_template("history.html", transactions_data = transactions_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get('symbol').strip()
        if symbol == "":
            return apology("must provide a symbol to quote", 400)

        #notice that lookup returns a dict in the form of {"name": symbol, "price": price, "symbol":symbol}
        price_data = lookup(symbol)

        if price_data == None:
            return apology("Invalid symbol")
        else:
            return render_template("quoted.html", symbol=price_data['symbol'], price=usd(price_data['price']), name=price_data['name'])
    else:
        return render_template("quote.html")

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

        user = request.form.get('username').strip()
        password = request.form.get('password').strip()
        pwd_confirm = request.form.get('confirmation').strip()

        if password == "":
            return apology("Must provide a password", 400)

        if user == "":
            return apology("Must provide username", 400)

        if password != pwd_confirm:
            return apology("Password confirmation does not match", 400)

        #print(db.execute("SELECT username FROM users WHERE username = ?;", user)[0]['username'])
        try:
            user_db = db.execute("SELECT username FROM users WHERE username = ?;", user)[0]['username'].strip()
        except:
            #all checks passed, hash pwd and insert user in users table and redirect to login
            hashpass = generate_password_hash(password)
            db.execute("INSERT INTO users (username, cash, hash) values(?, ?, ?);", user, 10000, hashpass)
            return render_template("login.html")
        else:
            if user_db == user:
                return apology("Username taken, please choose a different one", 400)
            else:
                #all checks passed, hash pwd and insert user in users table and redirect to login
                hashpass = generate_password_hash(password)
                db.execute("INSERT INTO users (username, cash, hash) values(?, ?, ?);", user, 10000, hashpass)
                return render_template("login.html")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        symbol = request.form.get('symbol')
        if symbol == "":
            return apology("must provide a symbol to sell", 403)
        try:
            shares = int(request.form.get('shares'))
        except ValueError:
            return apology("Shares must be a positive integer")
        else:
            if shares <= 0:
                return apology("Shares must be a positive integer")
            else:
                try:
                    #notice that lookup returns a dict in the form of {"name": symbol, "price": price, "symbol":symbol}
                    price_data = lookup(symbol)
                except:
                    return apology("Error retrieving price")
                else:
                    if price_data == None:
                        return apology("Invalid symbol")
                    else:
                        #check if user has enough shares to sell
                        user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])[0]['username']
                        shares_in_hand = db.execute("SELECT SUM(shares) AS shares FROM purchases WHERE username = ?;", user)[0]['shares']
                        print(shares_in_hand)

                        if shares  > shares_in_hand:
                            return apology("Not enough shares to sell")
                        else:
                            #make the sell: 1) create a register in table 'purchases' 2) increase the cash for the user in table 'users 3) return
                            cash = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])[0]['cash']
                            new_cash = cash + shares * price_data['price']
                            db.execute("INSERT INTO purchases (username, symbol, shares, share_price, time_stamp) values(?, ?, ?, ?, ?);", user, symbol, -shares, price_data['price'],datetime.now())
                            db.execute("UPDATE users SET cash = ? where id = ?;", new_cash, session["user_id"])
                            return redirect("/")

    else:
        symbols_ = db.execute("SELECT symbol FROM purchases GROUP BY symbol HAVING SUM(shares) > 0;")

        symbols = []
        for i in symbols_:
            symbols.append(i['symbol'])

        return render_template("sell.html", symbols = symbols)


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

