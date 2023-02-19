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


## Delete a game from the database DELETE
# Code to delete an existing game from the database by ID and return a JSON response
@games_bp.route("/<game_id>", methods=["DELETE"])
def delete_game(game_id):
    
    game = validate_model(Game, game_id)
    db.session.delete(game)
    db.session.commit()
    return make_response(f"Game #{game.id} successfully deleted")

# Code to retrieve data from the request body, update an existing game 
# in the database by ID, and return a JSON response
@games_bp.route("/<game_id>", methods=["PUT"])
def update_game(game_id):

    game = validate_model(Game, game_id)
    request_body = request.get_json()
    
    try: 
        #game.game_number=request_body["game_number"]
        game.player_a_score=request_body["player_a_score"]
        game.player_b_score=request_body["player_b_score"]                    
        game.set_id=request_body["set_id"]
        print("game_set_id",game.set_id)

        #game.game_winner=request_body["game_winner"]
        game.game_winner=game_done_game_winner(game)  #request_body["game_winner"] # 
        game.game_done=True
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))    
    
    db.session.commit()
    update_set_match_based_on_game_score(game)
    game_response = game.to_dict()
    #print("game_response.game_winner",game_response.game_winner)
    return jsonify(game_response),200


def game_done_game_winner(game):
    set_id = game.set_id
    print("set_id",set_id)
    cur_set = validate_model(Set, set_id)
    print("cur_set",cur_set)
    match_id = cur_set.match_id
    print("match_id",match_id)
    cur_match = validate_model(Match,match_id)
    if game.player_a_score == 4 and game.player_b_score <= 3:        
        player_a_id = cur_match.player_a_id
        cur_player1 = validate_model(Player,player_a_id)
        player_a_name = cur_player1.first_name
        game.game_winner = player_a_name
        return player_a_name
    if game.player_b_score == 4 and game.player_a_score <= 3:
        player_b_id = cur_match.player_b_id
        cur_player2 = validate_model(Player,player_b_id)
        player_b_name = cur_player2.first_name
        print("player_b_name",player_b_name)
        game.game_winner = player_b_name
        return player_b_name 

### Update set or match based on game winner
def update_set_match_based_on_game_score(game):
    set_id = game.set_id
    print("set_id",set_id)
    cur_set = validate_model(Set, set_id)
    print("cur_set",cur_set)
    match_id = cur_set.match_id
    print("match_id",match_id)
    cur_match = validate_model(Match,match_id)
    player_a_id = cur_match.player_a_id
    cur_player1 = validate_model(Player,player_a_id)
    player_a_name = cur_player1.first_name
    player_b_id = cur_match.player_b_id
    cur_player2 = validate_model(Player,player_b_id)
    player_b_name = cur_player2.first_name
    
    if game.game_winner == player_a_name:
        cur_set.player_a_games_won += 1   
    else:
        cur_set.player_b_games_won += 1

    print("player a games won", cur_set.player_a_games_won)    
    print("player b games won", cur_set.player_b_games_won)

    if cur_set.player_a_games_won == cur_match.no_of_gamesperset and cur_set.player_b_games_won < cur_match.no_of_gamesperset:
        cur_set.set_winner = player_a_name
        cur_set.set_done = True
    if cur_set.player_b_games_won == cur_match.no_of_gamesperset and cur_set.player_a_games_won < cur_match.no_of_gamesperset:
        cur_set.set_winner = player_b_name
        cur_set.set_done = True
    print("cur_set.set_winner",cur_set.set_winner)

### Update Match based on set winner

    if cur_set.set_winner == player_a_name:
        cur_match.player_a_sets_won += 1
        
    if cur_set.set_winner == player_b_name:
        cur_match.player_b_sets_won += 1

    print("Player a _sets won", cur_match.player_a_sets_won)
    print("Player b _sets won", cur_match.player_b_sets_won)

    if (int(cur_match.player_a_sets_won or 0) + int(cur_match.player_b_sets_won or 0)) == cur_match.no_of_sets:
        cur_match.match_done = True
    else:
        cur_match.match_done = False
    if cur_match.player_a_sets_won > cur_match.player_b_sets_won and cur_match.match_done:
        cur_match.match_winner = player_a_name
        
    if cur_match.player_b_sets_won > cur_match.player_a_sets_won and cur_match.match_done:
        cur_match.match_winner = player_b_name
        
    print("cur_match.match_winner", player_b_name)
    db.session.commit()
    return 