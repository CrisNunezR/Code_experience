from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL('sqlite:///birthdays.db')

@app.route("/")
def index():
    test1 = db.execute("SELECT * from birthdays;") #this returns a list of all the returned rows as dictonaries
    test = [{'name': 'cris'}, {'day' : 21}, {'month' : 'jan'}]
    #test = [1, 2]
    return render_template("index.html", test = test1)