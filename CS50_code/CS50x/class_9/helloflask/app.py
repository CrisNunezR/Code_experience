"""
flask training file

Notes:

@app.route("/") is a function is called a decorator. Decorators allow
you to take a basic function, like app.route, and extend its functionality
with something custom: the function you write after the decorator.
(You can read more about decorators if you want here:
https://realpython.com/primer-on-python-decorators/)

This line tells Flask that if an HTTP request comes in for “/”, the index
function should be run.
Note that, if we renamed the function to be homepage, this line would tell
Flask that —every time it receives an HTTP request for “/”—
it should run the 'homepage' function.

Notice that the index function returns a piece of text, “Hello, World!”.
This text is what Flask will render to the user when their request to
the “/” route is complete. The returned text could be (and often is!)
the text of an entire HTML file, which the browser then renders accordingly.
But it’s just a piece of text for now, for brevity’s sake.

To run your app, type flask run into the terminal, and you will get a
link to click, similar to when you run http-server.

You’ve written a Flask app! Try returning different text,
like <h1>Hello, World!</h1>. How does this change what you see?

"""


from flask import Flask
from flask import render_template, request #we need this methods to use html templates

app = Flask(__name__)


#@app.route("/") this is the basic @app instruction
@app.route("/", methods = ['GET', 'POST']) #this instruction allows for the use of GET and POST methods

def index():
    #this if-else structure is also needed to handle GET and POST
    if request.method == 'GET':
        return render_template('index.html')
    else:
        print('Form submitted')
        color = request.form.get('color') #this comes from the form via POST
        return render_template('color.html', color = color)

    #return "<h1>Hello, World!</h1>" #this was the initial code
    #return render_template("index.html") #this code now enables assigning html files but not GET-POST methods