from flask import Blueprint, jsonify, abort, make_response, request 
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model

games_bp = Blueprint("games_bp", __name__, url_prefix="/games")

# ## `POST /games`
# #@games_bp.route("/games", methods=["POST"])