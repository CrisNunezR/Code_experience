"""
This code enables Flask to operate with HTML
it imports:
    -The function 'flask'
    -enables the calling for templates (from the templates/ folder) that contains HTML files
    -request: is a variable built into the function
"""

from flask import Flask, render_template, request

app = Flask(__name__) #this line basically 'turns this file into a Flask application'

#with the code before we take control of the server and need to send something to display

@app.route("/") #this defines what code I want the page to execute when the used visits the initial page "/"
def index(): #this function is usually called 'index' since it's the main page of the site

    if "name" in request.args: #this is a variable I assign in the URL by entering "?name=Cris" at the end of the url
                                #notice that ?name defines the name of the variable and = Cris defines its value
        name = request.args["name"]
    else:
        name = "there"


    """notice that I can return a variable, text or, as with the 2nd example an HTML file using render_template"""
    #return "hello, there" #this sends plain text to the server
    #return render_template("index.html")    #this sends an HTML file to the server
    return render_template("index.html", ext_variable = name) #notice that I'm now asigning a variable to be read on the HTML

"""
now, to execute this code, we need to type this to execute Flask in the same folder where our app.py is:
        $ flask run
"""

 