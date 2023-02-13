from flask import Blueprint, jsonify, abort, make_response, request 
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model

players_bp = Blueprint("players_bp", __name__, url_prefix="/players")

## `POST /players`
#@players_bp.route("/players", methods=["POST"])