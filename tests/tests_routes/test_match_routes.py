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

@pytest.mark.skip()
def test_create_match(client, user, player):
    match_data = {
        "no_of_sets": 3,
        "no_of_gamesperset": 6,
        "match_name": "test_match",
        "player_a_id": player.id,
        "player_b_id": player.id,
        "user_id": user.id
    }
    response = client.post("/matches/match", json=match_data)
    assert response.status_code == 201
    assert response.get_data(as_text=True) == f"Match {match_data['match_name']} successfully created"

@pytest.mark.skip()
def test_get_all_matches(client, match):
    response = client.get("/matches/")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
    assert response.get_json()[0]["match_name"] == match.match_name

@pytest.mark.skip()
def test_get_match(client, match):
    response = client.get(f"/matches/{match.id}")
    assert response.status_code == 200
    assert response.get_json()["match_name"] == match.match_name

@pytest.mark.skip()
def test_update_match(client, match):
    new_match_name = "updated_test_match"
    match_data = {
        "no_of_sets": 5,
        "no_of_gamesperset": 7,
        "match_name": new_match_name,
        "player_a_id": match.player_a_id,
        "player_b_id": match.player_b_id,
        "user_id": match.user_id
    }
    response = client.put(f"/matches/{match.id}", json=match_data)
    assert response.status_code == 200
    assert response.get_json()["match_name"] == new_match_name

@pytest.mark.skip()
def test_delete_match(client, match):
    response = client.delete(f"/matches/{match.id}")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == f"match #{match.id} successfully deleted"
    assert Match.query.get(match.id) is None