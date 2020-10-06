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

# Home page route
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Contacts API</h1>
<p>A demo API for storing, updating, and reading personal contacts.</p>
'''


# A route to return all of the available contacts
@app.route('/contacts/all', methods=['GET'])
def api_all():
    return jsonify(contacts)

## READ ROUTES ##

# Redirect to /contacts/all if no id provided
@app.route('/contacts/')
def api_contacts():
    return api_all()

# A route to return a specific contact by id
@app.route('/contacts/<int:id>', methods=['GET'])
def api_byID(id):
    results = []
    for contact in contacts:
        if contact['id'] == id:
            results.append(contact)

    return jsonify(results)

# A route to add a contact
@app.route('/contacts', methods=['POST'])
def api_add():
    
    id = len(contacts)
    print(request.json)
    if 'fname' in request.json:
        fname = request.json['fname']
    else:
        fname = ''
    if 'lname' in request.json:
        lname = request.json['lname']
    else:
        lname = ''
    if 'email' in request.json:
        email = request.json['email']
    else:
        email = ''
    if 'phone' in request.json:
        phone = request.json['phone']
    else:
        phone = ''
    contact = {
        'id': id,
        'fname': fname,
        'lname': lname,
        'email': email,
        'phone': phone
    }
    contacts.append(contact)
    return jsonify({'contact': contact}), 201

# A route to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def api_delete(id):
    contact = [contact for contact in contacts if contact['id'] == id]
    if len(contact) == 0:
        return jsonify({'error': 'no contacts foudn with given id'}), 404
    contacts.remove(contact[0])
    return jsonify({'result': "deleted"})

# A route to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def api_update(id):
    contact = [contact for contact in contacts if contact['id'] == id]
    if len(contact) == 0:
        return jsonify({'error': 'no contacts foudn with given id'}), 404
    
    if 'fname' in request.json:
        contact[0]['fname'] = request.json['fname']

    if 'lname' in request.json:
        contact[0]['lname'] = request.json['lname']

    if 'email' in request.json:
        contact[0]['email'] = request.json['email']

    if 'phone' in request.json:
        contact[0]['phone'] = request.json['phone']
   
    return jsonify({'contact':contact[0]})

