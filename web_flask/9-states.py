#!/usr/bin/python3
"""
List all states, then select each state to list its cities
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the SQLAlchemy session"""
    storage.close()


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states(id=None):
    """List all states
    """
    states = storage.all(State).values()
    if not id:
        return render_template('9-states.html', state=states)
    else:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', state=state)
        return render_template('9-states.html')
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
