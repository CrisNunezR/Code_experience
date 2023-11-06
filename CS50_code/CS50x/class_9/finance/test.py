import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, login_required, lookup
from datetime import datetime
import threading

app = Flask(__name__)

# ... (other configurations)

# Configure CS50 Library to use SQLite database
db = sqlite3.connect("dudo.db")

class ReadUserNameThread(threading.Thread):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.result_data = None

    def run(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (self.username,))
        data = cursor.fetchall()
        cursor.close()
        db.close()
        self.result_data = data

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

        # Create and start the thread to read the username
        thread = ReadUserNameThread(request.form.get("username"))
        thread.start()
        thread.join()
        rows = thread.result_data

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
