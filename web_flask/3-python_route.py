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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
