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

@games_bp.route("/game", methods=["POST"])
def create_game():
    request_body = request.get_json()
    new_game = Game(game_number=request_body["game_number"],
                set_id=request_body["set_id"]
    )
    db.session.add(new_game)
    db.session.commit()

    return make_response(f"Game1 {new_game.game_number} successfully created", 201)

### Get All games
# Code to retrieve all games from the database and return as a JSON response
@games_bp.route("/", methods=["GET"])
def get_all_games():
    game_query = Game.query
    game_number_query = request.args.get("game_number")
    if game_number_query:
        game_query = game_query.filter(Game.game_number.ilike(f"%{game_number_query}%"))
        
    sort_query = request.args.get("sort")
    if sort_query:
        if sort_query == "desc":
            game_query = game_query.order_by(Game.game_number.desc())
        else:
            game_query = game_query.order_by(Game.game_number.asc())

    games = game_query.all()
    print(games)
    games_response = []
    for game in games:
        print(game)
        games_response.append(game.to_dict())
    return jsonify(games_response)

## Get one game by id
# Code to retrieve a single game by ID from the database and return as a JSON response
@games_bp.route("/<game_id>", methods=["GET"])
def get_game(game_id):    
    game = validate_model(Game, game_id)
    return game.to_dict()

# Code to retrieve data from the request body, update an existing game 
# in the database by ID, and return a JSON response
@games_bp.route("/<game_id>", methods=["PUT"])
def update_game(game_id):

    game = validate_model(Game, game_id)
    request_body = request.get_json()
    try: 
        game.game_number=request_body["game_number"],
        game.player_a_score=request_body["player_a_score"],
        game.player_b_score=request_body["player_b_score"],                    
        game.set_id=request_body["set_id"]
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))    

    db.session.commit()
    game_response = game.to_dict()
    return jsonify(game_response),200


## Delete a game from the database DELETE
# Code to delete an existing game from the database by ID and return a JSON response
@games_bp.route("/<game_id>", methods=["DELETE"])
def delete_game(game_id):
    
    game = validate_model(Game, game_id)
    db.session.delete(game)
    db.session.commit()
    return make_response(f"Game #{game.id} successfully deleted")

