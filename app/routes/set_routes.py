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
                match_id=request_body["match_id"])
    #             player_a_games_won = request_body["player_a_games_won"],
    #             player_b_games_won= request_body["player_b_games_won"],
    #             set_winner = request_body["set_winner"]

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
        set.player_b_games_won= request_body["player_b_games_won"]
        set.set_winner = request_body["set_winner"]
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
    return make_response(f"Set #{set_id} successfully deleted")


##************************************************************************
# ******************NESTED ROUTES FOR Stat MODEL**************************
## Create a stat of the player from set

@sets_bp.route("/<set_id>/stat", methods=["POST"])
def create_stat_for_player_after_set_done(set_id):
    request_body = request.get_json()
    set = validate_model(Set,set_id)
    new_stat = Stat(
            set_id=set_id,
            player_id=request_body["player_id"],
            aces=request_body["aces"],
            winners=request_body["winners"],
            double_faults=request_body["double_faults"],
            unforced_errors=request_body["unforced_errors"],
            forced_errors=request_body["forced_errors"],
            set_won = request_body["set_won"]
        )
    
    new_stat.set = set
    print("new_stat",new_stat)
    db.session.add(new_stat)
    db.session.commit()
    message = f"Stat for {new_stat.player_id} created with Set{set.set_number}"
    return make_response(jsonify(message), 201)

### Get All Stats for a certain set who has created those
# Code to retrieve all matches from the database and return as a JSON response
@sets_bp.route('/<set_id>/stats', methods=['GET'])
def get_all_stats_for_the_use(set_id):
    set = validate_model(Set,set_id)

    stats_response = []
    for stat in set.stats:
        print("stat", stat)
        stats_response.append(stat.to_dict())
    print("stats Response", stats_response)
    return jsonify(stats_response)
