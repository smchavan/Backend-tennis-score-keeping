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
                    #registered_at = datetime.now()
                    #player_names=request_body["player_names"],
                    #match_names=request_body["match_names"]
                    )
    db.session.add(new_user)
    db.session.commit()
    return make_response({"user_id":new_user.id},201)
    #return make_response(f"User {new_user.first_name} successfully created", 201)

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
##************************************************************************
# ******************NESTED ROUTES FOR USER MODEL**************************

### CREATE a MATCH from user dashboard
#### POST 

@users_bp.route("/<user_id>/match", methods=["POST"])
def add_new_match_to_user(user_id):
    user = validate_model(User, user_id)

    request_body = request.get_json()
    print("request Body",request_body)
    new_match = Match(
            no_of_sets=request_body["no_of_sets"],
            no_of_gamesperset=request_body["no_of_gamesperset"],
            #match_date=datetime.now(),
            match_name=request_body["match_name"],
            player_a_id=request_body["player_a_id"],
            player_b_id=request_body["player_b_id"],
            user_id=user_id
        )
    #new_match = Match.from_dict(request_body)
    
    new_match.user = user
    print("new_match",new_match)
    db.session.add(new_match)
    db.session.commit()

    message = f"Match {new_match.match_name} created with User{user.first_name}"
    return make_response(jsonify(message), 201)

### CREATE a PLAYER from user dashboard
#### POST 

@users_bp.route("/<user_id>/player", methods=["POST"])
def add_new_player_to_user(user_id):
    user = validate_model(User, user_id)

    request_body = request.get_json()
    new_player = Player(first_name=request_body["first_name"],
                    last_name=request_body["last_name"],
                    date_of_birth=request_body["date_of_birth"],
                    serve_style=request_body["serve_style"],
                    utr=request_body["utr"],
                    user_id=user_id)
    
    new_player.user = user
    print("new_player",new_player)
    db.session.add(new_player)
    db.session.commit()
    message = f"Player {new_player.first_name} created with User{user.first_name}"
    return make_response(jsonify(message), 201)


### Get All Matches for a certain user who has created those
# Code to retrieve all matches from the database and return as a JSON response
@users_bp.route('/<user_id>/matches', methods=['GET'])
def get_all_matches_for_the_use(user_id):
    user = validate_model(User,user_id)

    matches_response = []
    for match in user.matches:
        print("match", match)
        matches_response.append(match.to_dict())
    print("matches Response", matches_response)
    return jsonify(matches_response)
### Get All Players for a certain user who has created those
# Code to retrieve all players from the database and return as a JSON response
@users_bp.route('/<user_id>/players', methods=['GET'])
def get_all_players_for_the_use(user_id):
    user = validate_model(User,user_id)

    players_response = []
    for player in user.players:
        print("player", player)
        players_response.append(player.to_dict())
    print("matches Response", players_response)
    return jsonify(players_response)
