from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import users
import datetime

app = Flask(__name__)
api = Api(app)


class User(Resource):
	def __init__(self):
	   self.id = len(users) + 1
	   #get a list of users

	   #create a new user
	def post(self,username):
		user=[user for user in users if user["username"]==username]
		if len(user)==0:
			new_user={
						"id":self.id,
						"firstname":request.json["firstname"],
						"lastname":request.json["lastname"],
						"othernames":request.json["othernames"],
						"email":request.json["email"],
						"phonenumber":request.json["phonenumber"],
						"username":username,
						"registered":datetime.datetime.now(),
						"isAdmin":False
						}
			users.append(new_user)
			return make_response(jsonify({
		   	"status" : 201,
		   	"data" : users}),201)
		else:
			return make_response(jsonify({"status":409,"error":"the record exists"}),409)
		#get one user
	def get(self,username):
		user=[user for user in users if user["username"]==username]
		if len(user)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "user does not exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : user}),200)

	




