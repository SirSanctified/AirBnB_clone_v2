#!/usr/bin/python3
"""
List cities by states
"""

from models import storage, State, City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display cities by states"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
