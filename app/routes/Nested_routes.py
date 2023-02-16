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

### CREATE a MATCH from user dashboard
#### POST 

# @users_bp.route("/<user_id>/match", methods=["POST"])
# def add_new_match_to_user(user_id):
#     user = validate_model(User, user_id)

#     request_body = request.get_json()
#     print("request Body",request_body)
#     new_match = Match.from_dict(request_body)
#     new_match.user = user
#     print("new_match",new_match)
#     db.session.add(new_match)
#     db.session.commit()

#     message = f"Match {new_match.match_name} created with User{user.first_name}"
#     return make_response(jsonify(message), 201)

### CREATE a Player from user dashboard
#### POST 

# @users_bp.route("/<user_id>/player", methods=["POST"])
# def add_new_match_to_user(user_id):
#     user = validate_model(User, user_id)

#     request_body = request.get_json()
#     print("request Body",request_body)
#     new_match = Match.from_dict(request_body)
#     new_match.user_id = user_id

#     db.session.add(new_match)
#     db.session.commit()

#     message = f"Moon {new_match.name} created with Planet{user.name}"
#     return make_response(jsonify(message), 201)






# Get all matches for a particular user GET -- users/user_id/matches 
# Get 