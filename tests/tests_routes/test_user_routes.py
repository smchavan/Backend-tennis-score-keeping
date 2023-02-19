import json
import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.models.match_player import Match_player


def test_create_user(client):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "password"
    }
    response = client.post("/users/user", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201
    assert b'{"user_id":1} in response.data \n'

def test_get_all_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_user(client):
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
    db.session.add(user)
    db.session.commit()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json["first_name"] == user.first_name
    assert response.json["last_name"] == user.last_name
    assert response.json["email"] == user.email
    assert response.json["password"] == user.password

def test_update_user(client):
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
    db.session.add(user)
    db.session.commit()

    data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com",
        "password": "new_password"
    }
    response = client.put(f"/users/{user.id}", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 200
    assert response.json["first_name"] == data["first_name"]
    assert response.json["last_name"] == data["last_name"]
    assert response.json["email"] == data["email"]
    assert response.json["password"] == data["password"]

def test_delete_user(client):
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
    db.session.add(user)
    db.session.commit()

    response = client.delete(f"/users/{user.id}")
    assert response.status_code == 200
    assert b"successfully deleted" in response.data




def test_update_game(client):
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password")
    db.session.add(user)
    db.session.commit()

    player_data1 = {
        "first_name": "Nandini Chavan",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "serve_style": "Right-handed",
        "utr": 9.0,
        "user_id": 1
    }
    client.post("/players/player", json=player_data1)

    player_data2 = {
        "first_name": "Vedant Chavan",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "serve_style": "Right-handed",
        "utr": 5.0,
        "user_id": 1
    }
    client.post("/players/player", json=player_data2)


    # Create a match, set, and game to update
    match = Match(player_a_id=1, player_b_id=2, no_of_sets=1,no_of_gamesperset = 1,user_id = 1)
    set = Set(match_id=1, set_number=1)
    game = Game(set_id=1, game_number=1)

    db.session.add(match)
    db.session.add(set)
    db.session.add(game)
    db.session.commit()

    # Send a PUT request to update the game score
    response = client.put("/games/1", json={
        "player_a_score": 4,
        "player_b_score": 2
    })

    assert response.status_code == 200

    # Check that the game score was updated
    updated_game = Game.query.get(1)
    assert updated_game.player_a_score == 4
    assert updated_game.player_b_score == 2

    # Check that the set and match tables were also updated
    updated_set = Set.query.get(1)
    updated_match = Match.query.get(1)

    assert updated_set.player_a_games_won == 1
    assert updated_set.player_b_games_won == 0
    assert updated_set.set_winner == "Nandini Chavan"

    assert updated_match.player_a_sets_won == 1
    assert updated_match.player_b_sets_won == 0
    assert updated_match.match_winner == "Nandini Chavan"