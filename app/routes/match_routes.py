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
    print("matches REsponse", matches_response)
    return jsonify(matches_response)