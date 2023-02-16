from flask import Blueprint, jsonify, abort, make_response, request 
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model

sets_bp = Blueprint("sets_bp", __name__, url_prefix="/sets")

## Post or Create a new set
# Code to retrieve data from the request body, create a new set in the database, 
# and return a JSON response
@sets_bp.route("/set", methods=["POST"])

def create_set():
    request_body = request.get_json()
    new_set = Set(set_number=request_body["set_number"],
                match_id=request_body["match_id"]
    )
    db.session.add(new_set)
    db.session.commit()

    return make_response(f"Set1 {new_set.set_number} successfully created", 201)

### Get All sets
# Code to retrieve all sets from the database and return as a JSON response
@sets_bp.route("/", methods=["GET"])
def get_all_sets():
    set_query = Set.query
    set_number_query = request.args.get("set_number")
    if set_number_query:
        set_query = set_query.filter(Set.set_number.ilike(f"%{set_number_query}%"))
        
    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            set_query = set_query.order_by(Set.set_number.desc())
        else:
            set_query = set_query.order_by(Set.set_number.asc())

    sets = set_query.all()
    print(sets)
    sets_response = []
    for set in sets:
        print(set)
        sets_response.append(set.to_dict())
    return jsonify(sets_response)


## Get one set by id
# Code to retrieve a single set by ID from the database and return as a JSON response
@sets_bp.route("/<set_id>", methods=["GET"])
def get_set(set_id):    
    set = validate_model(Set, set_id)
    return set.to_dict()

# Code to retrieve data from the request body, update an existing set 
# in the database by ID, and return a JSON response
@sets_bp.route("/<set_id>", methods=["PUT"])
def update_set(set_id):

    set = validate_model(Set, set_id)
    request_body = request.get_json()
    try: 
        set.number = request_body["set_number"]
        set.match_id = request_body["match_id"]
        set.player_a_games_won = request_body["player_a_games_won"]
        set.player_a_games_won= request_body["player_a_games_won"]
        
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))    

    db.session.commit()
    set_response = set.to_dict()
    return jsonify(set_response),200

## Delete a set from the database DELETE
# Code to delete an existing set from the database by ID and return a JSON response
@sets_bp.route("/<set_id>", methods=["DELETE"])
def delete_set(set_id):
    
    set = validate_model(Set, set_id)
    db.session.delete(set)
    db.session.commit()
    return make_response(f"Set #{set.id} successfully deleted")
