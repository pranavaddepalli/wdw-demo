import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

contacts = [
	{'id': 0,
	'fname': 'Scotty',
	'lname': 'Labs',
	'phone': '0123456789',
	'email': 'hello@scottylabs.org'}
]

# Home page route
@app.route('/', methods=['GET'])
def  home():
	return  '''
	<h1>Contacts API</h1>
	<p>A demo API for storing, updating, and reading personal contacts.</p> 
	'''

# A route to return all of the available contacts
@app.route('/contacts/all', methods=['GET'])
def api_all():
	return jsonify(contacts)