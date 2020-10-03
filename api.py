import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
contacts = [
    {'id': 0,
     'fname': 'Pranav',
     'lname': 'Addepalli',
     'phone': '5715240967',
     'email': 'pranav.addepalli@gmail.com'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Contacts API</h1>
<p>A demo API for storing, updating, and reading persnoal contacts.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/contacts/all', methods=['GET'])
def api_all():
    return jsonify(contacts)

app.run()