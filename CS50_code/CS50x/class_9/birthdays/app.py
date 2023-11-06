"""

Complete the implementation of a web application to let users store and
keep track of birthdays.

When the / route is requested via GET, your web application should display,
in a table, all of the people in your database along with their birthdays.

First, in app.py, add logic in your GET request handling to query the birthdays.db
database for all birthdays. Pass all of that data to your index.html template.

Then, in index.html, add logic to render each birthday as a row in the table.
Each row should have two columns: one column for the person’s name and another
column for the person’s birthday.

When the / route is requested via POST, your web application should add a new
birthday to your database and then re-render the index page.

First, in index.html, add an HTML form. The form should let users type in a name,
a birthday month, and a birthday day. Be sure the form submits to / (its 'action')
with a method of post.

Then, in app.py, add logic in your POST request handling to INSERT a new row into
the birthdays table based on the data supplied by the user.

Optionally, you may also:
    Add the ability to delete and/or edit birthday entries.
    Add any additional features of your choosing!



Notice that the initial setting for the app.py is:
    Currently, when the / route is requested via GET,
    the index.html template is rendered. When the / route
    is requested via POST, the user is redirected back to / via GET

Content description:

birthdays.db is a SQLite database with one table, birthdays,
that has four columns: id, name, month, and day.
There are a few rows already in this table, though ultimately
your web application will support the ability to insert rows into this table!

The static directory is a styles.css file containing the CSS code
for this web application. No need to edit this file, though you’re welcome to if you’d like!

In the templates directory is an index.html file that will be rendered when the user
views your web application.

"""

import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
   #Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():

    #db.execute("INSET INTO birthdays (name, day, month) VALUES(?, ?, ?);", name, day, month)

    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get('name')

        #reads information from form in HTML
        try:
            day = int(request.form.get('day'))
        except ValueError:
            return render_template('index.html', message_day = "Enter a number between 1 and 31")
        try:
            month = int(request.form.get('month'))
        except ValueError:
            return render_template('index.html', message_day = "Enter a number between 1 and 12")

        #Insert new b-day into birthdays table
        db.execute("INSERT INTO birthdays (name, day, month) VALUES(?, ?, ?);", name, day, month)

        #Collect new info in table
        bday_data = db.execute("SELECT name, month, day from birthdays;") #returns as a dict data from birthday table in db DataBase

        #return new data to put in table on HTML
        return render_template("index.html", bday_data = bday_data)

    else: #assumes metho is 'GET'
        # TODO: Display the entries in the database on index.html
        bday_data = db.execute("SELECT name, month, day from birthdays;") #returns as a dict data from birthday table in db DataBase
        return render_template("index.html", bday_data = bday_data)


