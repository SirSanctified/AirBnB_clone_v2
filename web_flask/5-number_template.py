#!/usr/bin/python3
"""
Simple routing example
"""

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c(text):
    """Return  'C' followed by the value of the text variable"""
    t = text.replace('_', ' ')
    return 'C {}'.format(t)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python(text="is cool"):
    """Add route accepting argument, but has a default value"""
    t = text.replace('_', ' ')
    return 'Python {}'.format(t)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Check if n is integer and return 'n is a number' if true
    else return 404 page"""
    if isinstance(n, (int)):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    if isinstance(n, (int)):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
