from flask import Blueprint, request, jsonify
import json
import bson
import pymongo
import os
import sys
from pymongo import MongoClient
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)



connection = "mongodb+srv://yuval:Ap196719@cluster0.auksy.mongodb.net/flaskProject?retryWrites=true&w=majority"
client = MongoClient(connection)
db = client["flaskProject"]
collection = db["users"]


indexRoute = Blueprint("index", __name__)
createRoute = Blueprint("create", __name__)
createLogIn = Blueprint("login",__name__)


@indexRoute.route("/api/users")
def index():

	users = []
	cursor = collection.find({})
	for document in cursor:
		users.append({"_id":JSONEncoder().encode(document["_id"]),
		 "username": document["username"],
		 "password": document["password"],
		 "firstName": document["firstName"],
		 "lastName": document["lastName"],
		 "email": document["email"]})
	
	return jsonify(data=users)



@createRoute.route("/api/login", methods=['POST'])
def login():
	print(request.json, flush=True)

	username = request.json.get("username")
	password = request.json.get("password")

	users = []
	cursor = collection.find({})
	for document in cursor:
		users.append({"_id":JSONEncoder().encode(document["_id"]),"username": document["username"], "password": document["password"]})

	for user in users:
		if user["username"] == username and user["password"] == password:
			return jsonify(user)
		else:
			return jsonify(data = "no user access")
	
	return jsonify(data = username)



@createRoute.route("/api/created", methods=['POST'])
def create():
	print(request.json, flush=True)

	username = request.json.get("username")
	password = request.json.get("password")
	firstName = request.json.get("firstName")
	lastName = request.json.get("lastName")
	email = request.json.get("email")

	user = {
		"username":username,
	    "password":password,
	    "firstName":firstName,
	    "lastName":lastName,
	    "email":email,
	}

	collection.insert_one(user)

	return jsonify(data = user)





