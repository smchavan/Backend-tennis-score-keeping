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
            match_date=request_body["match_date"],
            match_name=request_body["match_name"],
            player_a_id=request_body["player_a_id"],
            player_b_id=request_body["player_b_id"],
            user_id=request_body["user_id"]
        )
    db.session.add(new_match)
    db.session.commit()
