#!/usr/bin/python3
"""Script that starts a Flask web application:
application will be listening on 0.0.0.0, port 5000

Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition

/c/<text>: display “C ” followed by the value
of the text variable (replace underscore _ symbols with a space )
"""
from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """a function to display Hello HBNB!"""

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    """says the string HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    """retuns the text parameter"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
