from flask import Blueprint, jsonify, abort, make_response, request 
from app import db
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.routes.routes_helper import validate_model

## Post or Create a new player
# Code to retrieve data from the request body, create a new player in the database, and return a JSON response
players_bp = Blueprint("players_bp", __name__, url_prefix="/players")
@players_bp.route('/player', methods=['POST'])
def create_player():
    request_body = request.get_json()
    new_player = Player(first_name=request_body['first_name'],
                    last_name=request_body['last_name'],
                    date_of_birth=request_body['date_of_birth'],
                    serve_style=request_body['serve_style'],
                    utr=request_body['utr'],
                    user_id=request_body['user_id'])
    db.session.add(new_player)
    db.session.commit()

    return make_response(f"Player {new_player.first_name} successfully created", 201)

### Get All Players
# Code to retrieve all players from the database and return as a JSON response
@players_bp.route('/', methods=['GET'])
def get_all_players():
    player_query = Player.query
    first_name_query = request.args.get("first_name")
    if first_name_query:
        player_query = player_query.filter(Player.first_name.ilike(f"%{first_name_query}%"))
        
    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            player_query = player_query.order_by(Player.first_name.desc())
        else:
            player_query = player_query.order_by(Player.first_name.asc())

    players = player_query.all()
    players_response = []
    for player in players:
        players_response.append(player.to_dict())
    return jsonify(players_response)

## Get one player by id
# Code to retrieve a single player by ID from the database and return as a JSON response
@players_bp.route('/<player_id>', methods=['GET'])
def get_player(player_id):    
    player = validate_model(Player, player_id)
    return player.to_dict()

# Code to retrieve data from the request body, update an existing player 
# in the database by ID, and return a JSON response
@players_bp.route('/<player_id>', methods=['PUT'])
def update_player(player_id):

    player = validate_model(Player, player_id)
    request_body = request.get_json()
    try: 
        player.first_name = request_body["first_name"]
        player.last_name = request_body["last_name"]
        player.date_of_birth = request_body["date_of_birth"]
        player.serve_style = request_body["serve_style"]
        player.utr = request_body["utr"]
        player.user_id = request_body["user_id"]
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))    

    db.session.commit()
    player_response = player.to_dict()
    return jsonify(player_response),200

## Delete a player from the database DELETE
# Code to delete an existing player from the database by ID and return a JSON response
@players_bp.route('/<player_id>', methods=['DELETE'])
def delete_player(player_id):
    
    player = validate_model(Player, player_id)
    db.session.delete(player)
    db.session.commit()
    return make_response(f"Player #{player.id} successfully deleted")