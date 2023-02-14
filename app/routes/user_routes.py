from flask import Blueprint, jsonify, abort, make_response, request 
from datetime import datetime
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model

users_bp = Blueprint("users_bp", __name__, url_prefix="/users")
## POST Create User
# Code to retrieve data from the request body, create a new user in the database, 
# and return a JSON response
@users_bp.route("/user", methods=["POST"])
def create_user():
    request_body = request.get_json()
    #new_user = User.from_dict(request_body)
    new_user = User(first_name=request_body["first_name"],
                    last_name=request_body["last_name"],
                    email=request_body["email"],
                    password=request_body["password"],
                    #registered_at = request_body["registered_at"],
                    #player_names=request_body["player_names"],
                    #match_names=request_body["match_names"]
                    )
    db.session.add(new_user)
    db.session.commit()

    return make_response(f"User {new_user.first_name} successfully created", 201)

## Get all users GET 
# Code to retrieve all users from the database and return as a JSON response
@users_bp.route("/", methods=["GET"])
def get_all_users():
    user_query = User.query
    first_name_query = request.args.get("first_name")
    if first_name_query:
        user_query = user_query.filter(User.first_name.ilike(f"%{first_name_query}%"))
        
    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            user_query = user_query.order_by(User.first_name.desc())
        else:
            user_query = user_query.order_by(User.first_name.asc())

    users = user_query.all()
    users_response = []
    for user in users:
        users_response.append(user.to_dict())
    return jsonify(users_response)

## Get one user by id
# Code to retrieve a single user by ID from the database and return as a JSON response
@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = validate_model(User, user_id)
    return user.to_dict()

## Update Existing User
# Code to retrieve data from the request body, update an existing user in the database by ID, 
# and return a JSON response
@users_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    
    user = validate_model(User, user_id)
    request_body = request.get_json()
    try: 
        user.first_name = request_body["first_name"]
        user.last_name = request_body["last_name"]
        user.email = request_body["email"]
        user.password = request_body["password"]
    
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))    

    #new_user = User.from_dict(request_body)

    db.session.commit()
    user_response = user.to_dict()
    return jsonify(user_response),200


## DELETE user by user_id
# Code to delete an existing user from the database by ID and return a JSON response
@users_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    
    user = validate_model(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return make_response(f"User #{user.id} successfully deleted")
