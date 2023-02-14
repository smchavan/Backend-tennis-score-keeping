from flask import Blueprint, jsonify, abort, make_response, request 
import datetime
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model


match_players_bp = Blueprint("match_players_bp", __name__, url_prefix="/match_players")