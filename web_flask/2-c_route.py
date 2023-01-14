#!/usr/bin/python3
"""
Simple routing example
"""

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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return  'C' followed by the value of the text variable"""
    t = text.replace('_', ' ')
    return 'C {}'.format(t)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
