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
