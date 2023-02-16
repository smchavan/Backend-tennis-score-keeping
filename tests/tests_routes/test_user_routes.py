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
    assert b"successfully created" in response.data

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