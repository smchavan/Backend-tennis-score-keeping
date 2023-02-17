from flask import Blueprint, jsonify, abort, make_response, request 
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model

stats_bp = Blueprint("stats_bp", __name__, url_prefix="/stats")

## Post or Create a new stat
# Code to retrieve data from the request body, create a new stat in the database, 
# and return a JSON response
@stats_bp.route("/stat", methods=["POST"])
def create_stat():
    request_body = request.get_json()
    new_stat = Stat(
            set_id=request_body["set_id"],
            player_id=request_body["player_id"],
            aces=request_body["aces"],
            winners=request_body["winners"],
            double_faults=request_body["double_faults"],
            unforced_errors=request_body["unforced_errors"],
            forced_errors=request_body["forced_errors"],
            set_won=request_body["set_won"]
        )
    db.session.add(new_stat)
    db.session.commit()
    
    return make_response(f"Stat for set {new_stat.set_id} successfully created", 201)

### Get All Stats
# Code to retrieve all stats from the database and return as a JSON response
@stats_bp.route('/', methods=['GET'])
def get_all_stats():
    stat_query = Stat.query
    # stat_player_id_query = request.args.get("player_id")
    # if stat_player_id_query:
    #     stat_query = stat_query.filter(Stat.stat_player_id.ilike(f"%{stat_player_id_query}%"))
        
    # sort_query = request.args.get("sort")
    # if sort_query:
    #     if sort_query == "desc":
    #         stat_query = stat_query.order_by(Stat.stat_name.desc())
    #     else:
    #         stat_query = stat_query.order_by(Stat.stat_name.asc())
    
    stats = stat_query.all()
    print("stats", stats)
    stats_response = []
    for stat in stats:
        print("stat", stat)
        stats_response.append(stat.to_dict())
    print("states Response", stats_response)
    return jsonify(stats_response)

## Get one stat by id
# Code to retrieve a single stat by ID from the database and return as a JSON response
@stats_bp.route("/<stat_id>", methods=["GET"])
def get_stat(stat_id):    
    stat = validate_model(Stat, stat_id)
    return stat.to_dict()


# Code to retrieve data from the request body, update an existing stat 
# in the database by ID, and return a JSON response
@stats_bp.route("/<stat_id>", methods=["PUT"])
def update_stat(stat_id):

    stat = validate_model(Stat, stat_id)
    request_body = request.get_json()
    try: 
        stat.set_id = request_body["set_id"]
        stat.player_id = request_body["player_id"]
        stat.aces = request_body["aces"]
        stat.winners = request_body["winners"]
        stat.double_faults = request_body["double_faults"]
        stat.unforced_errors = request_body["unforced_errors"]
        stat.forced_errors = request_body["forced_errors"]
        stat.set_won = request_body["set_won"]
        
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))    

    db.session.commit()
    stat_response = stat.to_dict()
    return jsonify(stat_response),200

## Delete a stat from the database DELETE
# Code to delete an existing statfrom the database by ID and return a JSON response
@stats_bp.route("/<stat_id>", methods=["DELETE"])
def delete_stat(stat_id):
    
    stat= validate_model(Stat, stat_id)
    db.session.delete(stat)
    db.session.commit()
    return make_response(f"Stat #{stat.id} successfully deleted")

