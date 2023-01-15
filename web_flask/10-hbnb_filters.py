#!/usr/bin/python3
"""Filter searches on the page"""


from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Filter cities, states and amenities
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
