# Lab: Building a RESTful Contacts API with Flask
In this lab, you’ll use Flask, a popular Python web framework, to build a RESTful API.

## Overview
The goal of this lab is to create an API that will allow us to make perform the basic operations of REST -- creating, reading updating, and deleting. This lab is a derivation of [Miguel Grinberg’s Flask RESTFul API Tutorial](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask), modified specifically for ScottyLabs WDW. The code for this walk-through is hosted on [GitHub](https://github.com/pranavaddepalli/wdw-demo), and if you want to see the API live, check out the [demo](https://github.com/pranavaddepalli/wdw-demo/tree/demo) branch!

## Diving In
The code and tutorial for this lab will be [hosted on GitHub](https://github.com/pranavaddepalli/wdw-demo). The code for each step is also given at the end of the step.
Make sure you go over the  [basic concepts](https://docs.google.com/presentation/d/1PTjdVvNFjh2FI64JupVmVFjXdqBEltiEaRV5EcblGTI/edit?usp=sharing) from the WDW talk: we’ll be using some terms here that you may not be familiar with, and it’s a good idea to brush up on these first. If you'd like, you can also check out the talk's [recording]( ).
In addition, before these steps, you should download  [Python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/), and [Postman](https://www.postman.com/downloads/). Make sure you have an editor as well!

## 1. Getting Started - Installation and Setup
The first step takes care of setup and running a basic ‘Hello, World!’ application.

Flask requires a specific structure for your application to run correctly, so we’ll begin by creating the structure for our API using the terminal. Create a new folder, and let's just call it  `wdwflask`:
```
$ mkdir wdwflask
$ cd wdwflask
```

We will now create a virtual environment using  `venv`. First, install the `virtualenv` module by running 
```
$ python3 -m pip install virtualenv
```
Then, run the command
```
$ python3 -m venv env
```
This creates a virtual environment at  `wdwflask/env` . This might be a bit confusing, but it essentially isolates our project from any other python that you have on your computer so that we can have our own dependencies. Let's activate the virtual environment.

Windows:
```
$ . env\Scripts\activate.bat
```
MacOS/Unix:
```
source env/bin/activate
```
Your terminal should now look like
```
$ (env)
```
Let's install flask. Run the following command:
```
$ pip install flask
```
We can now create our basic application structure. Create an `app` folder in your `wdwflask` directory, where we'll be putting our API:
```
$ mkdir app
```
Now let’s get to the actual application! Let’s start by creating an initialization script. Open up your favorite editor -- I use VSCode -- and create a file in `wdwflask` called `wsgi.py`.
```python
from app.main import app

if  __name__ == "__main__":
	app.run()
```
When we test our API, we'll be running this file. It tells Flask to run using a file called `main` -- so let's create it!

Under the `app` folder, create `main.py`:
```python
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
```
The script above creates the application object of class Flask and then imports the `requests` and `jsonify` modules, which we'll be using later. We've also set Flask to run in debug mode, which means it'll tell us where an error occurs. **It also restarts the server every time we save our code!**

To start building our API, let's add the function we designed during the presentation:
```python
@app.route('/', methods=['GET'])
def  home():
	return  "Hello, world!"
```
Here, we're telling Flask that if a `GET` request is sent to the `'/'` URL, or the root, then respond with the string `"Hello, world!"`.

To run our server, go to your terminal and make sure that you're in `wdwflask` (and not in `/app`). Start the server by running
```
$ python3 wsgi.py
```
Now, go to `localhost:5000` in your browser. You should be able to see the result!
If you enter any other URL than `‘/’` you will get an error, since it is the only URL that has been defined so far.

Let's set up Postman to make building our API easier. Postman is a GUI that lets you test API requests and responses with a clean interface and a set of organized tools. Web browsers are not easily able to generate all types of HTTP requests, so using a tool like Postman will help us once we get into `POST`, `PUT`, and `DELETE`.

Make sure that your API server is still running, and then launch Postman. There's no need to sign in, but you can if you wish.

Click the '+' icon in the middle of the screen to open a new 'tab' for a request. It will be set to a GET request by default, which is what we want. Type in `localhost:5000` in the URL box, and then hit send. 

You should be able to see `"Hello, world!"` again! [Here's what it should look like.](https://raw.githubusercontent.com/pranavaddepalli/wdw-demo/demo/Screen%20Shot%202020-10-06%20at%203.57.43%20PM.png)

**The code for this step is available [here](https://github.com/pranavaddepalli/wdw-demo/tree/main/step%201).**

## 2. Implementing RESTFul Services
In this step, we'll be creating our contacts database and adding some API services.

Let's start by changing the API's home page since it's going to be the only response in pure text. In `main.py`, edit `home()`:

```python
def  home():
	return  '''
	<h1>Contacts API</h1>
	<p>A demo API for storing, updating, and reading personal contacts.</p> 
	'''
```
Here, we're returning some basic HTML so the page looks a little cleaner. It won't change anything with the API, so we're done with the `'/'` route.

Now, we're going to need to build our contacts database. To keep things simple, we keep this in Python by using a list of dictionaries.

In our representation, each element of the list is a contact. Every contact is represented as a dictionary with key-value pairs that represent different fields of information that we'd like to store.

In this lab, we'll be using four basic information fields:
- First name
- Last name
- Phone number
- Email

We'll also need to have a unique `id` for each contact. In addition, you should add your own fields to the contacts book! If you can't think of any, here's a couple examples:
- Birthday
- Nickname
- Address
- Instagram handle
- Favorite contact
- Website

Once you've decided which fields you'd like to use in addition to the four basic ones, you can initialize your contacts book with one contact:
```python
contacts = [
	{'id': 0,
	'fname': 'Scotty',
	'lname': 'Labs',
	'phone': '0123456789',
	'email': 'hello@scottylabs.org'}
]
```

In order to see our contacts, we can add our first API service -- the READ operation from CRUD. If you recall, this means we'll have to accept a `GET` request, so let's define a new route in `main.py`:
```python
# A route to return all of the available contacts
@app.route('/contacts/all', methods=['GET'])
def api_all():
	return jsonify(contacts)
```
That's all we need!
This tells Flask that if a `GET` request is sent to the `'/contacts/all'` URL, then it should call the `api_all()`  function. 

Since we're going to be returning data, in order for our API to follow REST principles, we need to serialize our data. Luckily, Flask's `jsonify` function can do this for us from a given data structure, turning it into JSON (JavaScript Object Notation), the standard format for data transfer.

Once you save your code, the server should automatically restart. Go to Postman and change the URL of the `GET` request to `localhost:5000/contacts/all`.

Hit send, and the contact should appear, [like this](https://raw.githubusercontent.com/pranavaddepalli/wdw-demo/main/step%202/Screen%20Shot%202020-10-06%20at%205.03.18%20PM.png)!

Congrats! You've just made your first API.

**The code for this step is available [here](https://github.com/pranavaddepalli/wdw-demo/tree/main/step%202).**

## 3. CRUD

In this step, we'll be implementing the other basic operations of a RESTful API -- CREATE, UPDATE, and DELETE.  We'll also be adding another READ function for individual contacts.

### READ

Being able to see all of our contacts is great, but in some cases, it's more useful to get information about a specific contact. To do that, let's add a route for us to send the `id` of a contact and receive that specific contact back.

Under REST, our API should be designed so that all of our functions can be accessed from the `'/contacts/` route. Remember that `GET` requests append the query parameters to the URL, so a request for a specific contact would be sent to the following URL:

`'/contacts/<int: id>` 

We can use the integer `id` provided in the URL to get the return information for the given contact by `id`. But before we dive into that, what if no id is provided?

To combat this, we'll just redirect `GET` requests to `'/contacts/'` by calling the `api_all()` function from earlier:
```python
# Redirect to /contacts/all if no id provided
@app.route('/contacts/')
def api_contacts():
	return api_all()
```
Now, we can look at the case where an `id` is provided. With the `<int: id>` syntax, Flask understands that `id` is an integer query parameter and will pass it to the function when it calls it. So, we'll have to add `id` as a parameter for our `api_byID` function:

```python
# A route to return a specific contact by id
@app.route('/contacts/<int:id>', methods=['GET'])
def api_byID(id):
	results = []
	for contact in contacts:
		if contact['id'] == id:
			results.append(contact)
	return jsonify(results)
```
In case something goes wrong and two contacts have the same `id`, we designed the function so that it will return all contacts with the given `id`.

Let's test this using Postman. Send a `GET` request to `'localhost:5000/contacts/0`, and our initial contact should appear! If you play around with other ids, you'll see that the API responds with an empty list.

### CREATE

Well, this doesn't really add much to our API. We can look at our Scotty Labs contact in two different ways, but that's about it. Let's add another contact to our database by looking at the next function of APIs -- **CREATE**.

In order to CREATE, we need to send data to our API. This means we'll have to use a `POST` request. Remember that `POST` requests include request data in the body, so we'll have to use that data to create a new contact.

Since JSON is the standard data format for RESTful APIs, we'll design our function assuming that the request has JSON body. Flask has a quick, built in way for us to access this: `request.json`.

In our function, we also need to account for the cases where not all parameters are given. In some calls to the API, we may only specify the first name, while in others, we give all of the fields. We can do this by conditionally checking for each field in the request, and assigning it to a new contact dictionary before appending it to the contact list.

We also need to add a unique `id` for each contact, but we can do this by just simply assigning it to the length of the contacts array. There are some potential problems with this method, but this won't severely affect our API.

Our function then looks something like this:
``` python
# A route to add a contact
@app.route('/contacts', methods=['POST'])
def api_add():
	id = len(contacts)
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
```
Let's test this in Postman. Click on the '+' to open a new tab, then select `POST` from the dropdown request type. Make sure the URL is `'localhost:5000/contacts'`, and then click on body. Click on raw, and then change the dropdown to JSON. 

Here, we can add the parameters that we are going to send as a part of this request. You can use this template, deleting the fields you don't need and adding the fields you do need, to create your JSON request:
```json
{"fname":"Andrew", "lname":"Carnegie", "email":"andrew@andrew.cmu.edu", "phone":"0000000000"}
```
In addition, you can use [JSON Lint](https://jsonlint.com/) to validate your JSON before you send the request. Once you do send the request, you should get a response with the contact you just added. If you go back to the `GET` request tab and send a request to see all the contacts, the contact you just added should now show up!

### UPDATE and DELETE

Updating a contact requires using the `PUT` request.  `PUT` requests are very similar to `POST` requests in that the data that we want to update is in the body of our request, but the request itself is sent to a specific contact.

This means we'll have to use a route to a specific contact to call our update function, just like how we did with `get_byID`. The logic behind our update function follows the same as our create function in that we exhaustively check for each parameter before updating the data.
```python
# A route to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def api_update(id):
	contact = [contact for contact in contacts if contact['id'] == id]
	if len(contact) == 0:
		return jsonify({'error': 'no contacts found with given id'}), 404
	if 'fname' in request.json:
		contact[0]['fname'] = request.json['fname']
	if 'lname' in request.json:
		contact[0]['lname'] = request.json['lname']
	if 'email' in request.json:
		contact[0]['email'] = request.json['email']
	if 'phone' in request.json:
		contact[0]['phone'] = request.json['phone']
	return jsonify({'contact':contact[0]})
```

Deleting a contact uses `DELETE`, which is a lot more straightforward than the other requests. If a `DELETE` request is sent to a specific contact, that contact is deleted.
``` python
# A route to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def api_delete(id):
	contact = [contact for contact in contacts if contact['id'] == id]
	if len(contact) == 0:
		return jsonify({'error': 'no contacts found with given id'}), 404
	contacts.remove(contact[0])
	return jsonify({'result': "deleted"})
```

To test `UPDATE` and `DELETE`, use a similar method to how we tested `POST` and `GET`. The URL will be `'localhost:5000/<int: id>'` for both types of requests, but for `UPDATE`, a request body similar to that of `POST` has to be used.

You now have a working, RESTful API in Flask. But you're not done!

**The code for this step is available [here](https://github.com/pranavaddepalli/wdw-demo/tree/main/step%203).**

## Going Forward: Independent Task

This API ultimately lets us store, read, and manipulate a "contact book." However, the only way to read data from the contact book is to either look at every contact, or provide an ID for the contact. 

Requiring an ID to be given is complicated and is not something that someone would want to do if they were to use our API. To even get the ID for the contact they are looking for, they would have to get all contacts, then search all of the contacts for the right one, and then extract the ID -- but at that point, there's no need in returning an individual contact!

Your task is to simplify this process by creating a `query` function. An API query call should allow someone to give some parameters that they want to search for -- for example, the last name "Carnegie" -- and the API should return all instances of contacts that match those parameters.

As a getting started hint, calling this function would involve sending a `GET` request to `'/contacts/query'`.


## Further Steps

Hopefully after this lab, you understand the basics of creating a RESTful API in Flask. 

As a disclaimer, this lab's API is not a fully RESTful API -- we didn't go over things like error handling, database integration, validation, and many more. There's also a small bug in the ID generation. See if you can catch it and fix it!

These topics are a little more complicated, but hopefully this lab has given you the basic building blocks to get started on those types of tasks.  [Miguel Grinberg’s tutorial](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)  goes over these things, and I highly suggest you go through that tutorial for further API development with Flask.

Most importantly -- I hope you had fun during this lab! It was definitely a great experience for me to put this together for you all, and I hope that this sparked an interest in APIs or software engineering as a whole for at least some of you. Whether you learned something or not, if you had fun working on this project, then that's good enough!

Thanks!
