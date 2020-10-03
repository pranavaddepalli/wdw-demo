import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some starting data as a simple list of dictionaries
contacts = [
    {'id': 0,
     'fname': 'Scotty',
     'lname': 'Labs',
     'phone': '0123456789',
     'email': 'hello@scottylabs.org'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Contacts API</h1>
<p>A demo API for storing, updating, and reading persnoal contacts.</p>'''


# A route to return all of the available contacts
@app.route('/contacts/all', methods=['GET'])
def api_all():
    return jsonify(contacts)

## LOOKUP ROUTES ##

# A route to return a specific contact by id
@app.route('/contacts/getbyID', methods=['GET'])
def api_byID():
    if 'id' in request.args:
        id = int(request.args['id'])
    results = []
    for contact in contacts:
        if contact['id'] == id:
            results.append(contact)

    return jsonify(results)

# A route to return a specific contact by first name
@app.route('/contacts/getbyfname', methods=['GET'])
def api_getbyfname():
    if 'fname' in request.args:
        fname = request.args['fname']
    else:
         fname = ''
    results = []
    for contact in contacts:
        if contact['fname'] == fname:
            results.append(contact)

    return jsonify(results)

# A route to return a specific contact by last name
@app.route('/contacts/getbylname', methods=['GET'])
def api_getbylname():
    if 'lname' in request.args:
        lname = request.args['lname']
    else:
        lname = ''
    results = []
    for contact in contacts:
        if contact['lname'] == lname:
            results.append(contact)

    return jsonify(results)

# A route to return a specific contact by first and last name
@app.route('/contacts/getbyflname', methods=['GET'])
def api_getbyflname():
    if 'lname' in request.args:
        lname = request.args['lname']
    else:
        lname = ''
    if 'fname' in request.args:
        fname = request.args['fname']
    else:
        fname = ''
    results = []
    for contact in contacts:
        if contact['fname'] == fname and contact['lname'] == lname:
            results.append(contact)

    return jsonify(results)

## DATA FUNCTIONS ##

# A route to add a contact
@app.route('/contacts/add', methods=['GET'])
def api_add():
    id = len(contacts)
    contacts.append({})
    contacts[id]['id'] = id
    if 'fname' in request.args:
        contacts[id]['fname'] = request.args['fname']
    if 'lname' in request.args:
        contacts[id]['lname']  = request.args['lname']
    if 'phone' in request.args:
        contacts[id]['phone']  = request.args['phone']
    if 'email' in request.args:
        contacts[id]['email']  = request.args['email']
    
    return jsonify(contacts[id])

# A route to delete a contact by id
@app.route('/contacts/delete', methods=['GET'])
def api_delete():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'no ID provided -- no contact deleted'
    results = []
    for contact in contacts:
        if contact['id'] == id:
            results.append(contacts.pop(id))

    return jsonify(results)

# A route to update a contact by id
@app.route('/contacts/update', methods=['GET'])
def api_update():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'no ID provided -- no contact updated'
    
    if 'fname' in request.args:
        contacts[id]['fname'] = request.args['fname']
    if 'lname' in request.args:
        contacts[id]['lname']  = request.args['lname']
    if 'phone' in request.args:
        contacts[id]['phone']  = request.args['phone']
    if 'email' in request.args:
        contacts[id]['email']  = request.args['email']
    
    return jsonify(contacts[id])

# A route to 