#!/usr/bin/python3
"""Script that starts a Flask web application:
application will be listening on 0.0.0.0, port 5000

Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value
        of the text variable (replace underscore _ symbols with a space )
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text="is cool"):
    """retuns the text parameter"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """returns n and if n is a number """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_to_html(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
