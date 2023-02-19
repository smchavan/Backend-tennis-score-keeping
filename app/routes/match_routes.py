from datetime import datetime
from flask import Blueprint, jsonify, abort, make_response, request 
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model

matchs_bp = Blueprint("matchs_bp", __name__, url_prefix="/matches")

# ## `POST /matchs`
# #@matchs_bp.route("/matchs", methods=["POST"])

# Create a new match - POST
@matchs_bp.route("/match", methods=["POST"])
def create_match():
    request_body = request.get_json()
    new_match = Match(
            no_of_sets=request_body["no_of_sets"],
            no_of_gamesperset=request_body["no_of_gamesperset"],
            #match_date=datetime.now(),
            match_name=request_body["match_name"],
            player_a_id=request_body["player_a_id"],
            player_b_id=request_body["player_b_id"],
            user_id=request_body["user_id"]
            # match_winner = request_body["match_winner"],
            # player_a_sets_won = request_body["player_a_sets_won"],
            # player_b_sets_won = request_body["player_a_sets_won"]
        )
    db.session.add(new_match)
    db.session.commit()
    
    return make_response(f"Match {new_match.match_name} successfully created", 201)

    ### Get All Matches
# Code to retrieve all matches from the database and return as a JSON response
@matchs_bp.route('/', methods=['GET'])
def get_all_matches():
    match_query = Match.query
    match_name_query = request.args.get("match_name")
    if match_name_query:
        match_query = match_query.filter(Match.match_name.ilike(f"%{match_name_query}%"))
        
    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            match_query = match_query.order_by(Match.match_name.desc())
        else:
            match_query = match_query.order_by(Match.match_name.asc())
    
    matches = match_query.all()
    print("matches", matches)
    matches_response = []
    for match in matches:
        print("match", match)
        matches_response.append(match.to_dict())
    print("matches Response", matches_response)
    return jsonify(matches_response)

## Get one match by id
# Code to retrieve a single match by ID from the database and return as a JSON response
@matchs_bp.route("/<match_id>", methods=["GET"])
def get_match(match_id):    
    match = validate_model(Match, match_id)
    return match.to_dict()

# Code to retrieve data from the request body, update an existing match 
# in the database by ID, and return a JSON response
@matchs_bp.route("/<match_id>", methods=["PUT"])
def update_match(match_id):

    match = validate_model(Match, match_id)
    request_body = request.get_json()
    try: 
        match.no_of_sets=request_body["no_of_sets"],
        match.no_of_gamesperset=request_body["no_of_gamesperset"],
        match.match_name=request_body["match_name"],
        match.player_a_id=request_body["player_a_id"],
        match.player_b_id=request_body["player_b_id"],
        match.user_id=request_body["user_id"],
        match.match_winner = request_body["match_winner"],
        match.player_a_sets_won = request_body["player_a_sets_won"],
        match.player_a_sets_won = request_body["player_a_sets_won"]

    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))    

    db.session.commit()
    match_response = match.to_dict()
    return jsonify(match_response),200

## Delete a match from the database DELETE
# Code to delete an existing match from the database by ID and return a JSON response
@matchs_bp.route("/<match_id>", methods=["DELETE"])
def delete_match(match_id):
    
    match = validate_model(Match, match_id)
    db.session.delete(match)
    db.session.commit()
    return make_response(f"match #{match.id} successfully deleted")


##***************************************NESTED ROUTES FOR CREATING SET *****************************************
#******Create a new set with match id ***************************************************************************

@matchs_bp.route("/<match_id>/set", methods=["POST"])
def add_new_set_to_match(match_id):
    match = validate_model(Match, match_id)

    request_body = request.get_json()
    print("request Body",request_body)
    new_set = Set(set_number=request_body["set_number"],
                    match_id=match_id)
    
    new_set.match = match

    db.session.add(new_set)
    db.session.commit()

    return make_response({"Set_id":new_set.id},201)

@matchs_bp.route('/<match_id>/sets', methods=['GET'])
def get_all_sets_for_the_match(match_id):
    match = validate_model(Match, match_id)
    sets_response = []
    for set in match.sets:
        print("set", set)
        sets_response.append(set.to_dict())
    print("Sets Response", sets_response)
    return jsonify(sets_response)




