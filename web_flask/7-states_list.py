#!/usr/bin/python3
"""
List all the states from the DBStorage engine
"""
from models import storage, storage.all
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Remove the current SQLAlchemy Session after each request

    Args:
        exception (Exception): any exception
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Render a template displaying a list of states available in storage
    """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
