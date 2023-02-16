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


def test_create_player(client, app):
    player_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "serve_style": "Right-handed",
        "utr": 5.0,
        "user_id": 1
    }
    response = client.post("/players/player", json=player_data)
    assert response.status_code == 201
    assert "successfully created" in response.get_data(as_text=True)

def test_get_all_players(client, app):
    response = client.get("/players/")
    assert response.status_code == 200
    assert len(json.loads(response.get_data(as_text=True))) == 0

    # create a new player
    player_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "serve_style": "Right-handed",
        "utr": "5.0",
        "user_id": 1
    }
    client.post("/players/player", json=player_data)

    response = client.get("/players/")
    assert response.status_code == 200
    assert len(json.loads(response.get_data(as_text=True))) == 1

def test_get_player(client, app):
    # create a new player
    player_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "serve_style": "Right-handed",
        "utr": "5.0",
        "user_id": 1
    }
    response = client.post("/players/player", json=player_data)
    player_id = response.get_data(as_text=True).split("#")[-1]

    response = client.get(f"/players/{player_id}")
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True))["id"] == int(player_id)

def test_update_player(client, app):
    # create a new player
    player_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "serve_style": "Right-handed",
        "utr": "5.0",
        "user_id": 1
    }
    response = client.post("/players/player", json=player_data)
    player_id = response.get_data(as_text=True).split("#")[-1]

    # update the player
    updated_player_data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "serve_style": "Right-handed",
        "utr": "5.0",
        "user_id": 1
    }
    response = client.put(f"/players/{player_id}", json=updated_player_data)
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True))["first_name"] == "Jane"

def test_delete_player(client):
    player = Player(first_name="John", last_name="Doe", date_of_birth = "1990-01-01", serve_style= "Right-handed",utr = 5.0,user_id = 1)
    db.session.add(player)
    db.session.commit()
    player_id = response.get_data(as_text=True).split("#")[-1]
    response = client.delete(f"/player/<player.id>")

    assert response.status_code == 200
    assert b"successfully deleted" in response.data

