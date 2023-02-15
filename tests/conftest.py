import pytest
from app import create_app
from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.models.match_player import Match_player

from app import db
from datetime import datetime
from flask.signals import request_finished

USER_FIRST_NAME1 = " First NAme of TEST User1"
USER_LAST_NAME1 = "Last Name Of Test User1"
USER_EMAIL1 = "xxxxxxxx"
USER_PASSWORD1 = "yyyyyyyyyy"

USER_FIRST_NAME2 = " First NAme of TEST User2"
USER_LAST_NAME2 = "Last Name Of Test User2"
USER_EMAIL2 = "ppppppppp"
USER_PASSWORD2 = "qqqqqqqqqq"

PLAYER_FIRST_NAME1 = " First Name of TEST player 1"
PLAYER_LAST_NAME1 = " Last Name of TEST player 1"
PLAYER_DATE_OF_BIRTH1 = "88888888"
PLAYER_UTR1 = 6
PLAYER_SERVE_STYLE1 = "LEFT"

PLAYER_FIRST_NAME2 = " First Name of TEST player 2"
PLAYER_LAST_NAME2 = " Last Name of TEST player 2"
PLAYER_DATE_OF_BIRTH2 = "5555555555"
PLAYER_UTR2 = 12
PLAYER_SERVE_STYLE2 = "RIGHT"

MATCH_NAME1 = "VD AND Nandini 1"
MATCH_PLAYER_A_ID1 = 1
MATCH_PLAYER_B_ID1 = 1
MATCH_USER_ID1 = 1
MATCH_NO_OF_SETS1 = 3
MATCH_NO_OF_GAMESPERSET1 = 6

MATCH_NAME2 = "VD AND Nandini 2"
MATCH_PLAYER_A_ID2 = 2
MATCH_PLAYER_B_ID2 = 3
MATCH_USER_ID2 = 2
MATCH_NO_OF_SETS2 = 3
MATCH_NO_OF_GAMESPERSET2 = 4

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_user(app):
    new_user1 = User(
        first_name = USER_FIRST_NAME1,
        last_name = USER_LAST_NAME1,
        email = USER_EMAIL1,
        password = USER_PASSWORD1
    )
    db.session.add(new_user1)
    db.session.commit()

@pytest.fixture
def second_user(app):
    new_user2 = User(
        first_name = USER_FIRST_NAME2,
        last_name = USER_LAST_NAME2,
        email = USER_EMAIL2,
        password = USER_PASSWORD2
    )
    db.session.add(new_user2)
    db.session.commit()

@pytest.fixture
def one_player(app):
    new_player1 = Player(
        first_name = PLAYER_FIRST_NAME1,
        last_name = PLAYER_LAST_NAME1,
        date_of_birth = PLAYER_DATE_OF_BIRTH1,
        serve_style = PLAYER_SERVE_STYLE1,
        utr = PLAYER_UTR1
    )
    db.session.add(new_player1)
    db.session.commit()

@pytest.fixture
def second_player(app):
    new_player2 = Player(
        first_name = PLAYER_FIRST_NAME2,
        last_name = PLAYER_LAST_NAME2,
        date_of_birth = PLAYER_DATE_OF_BIRTH2,
        serve_style = PLAYER_SERVE_STYLE2,
        utr = PLAYER_UTR2
    )
    db.session.add(new_player2)
    db.session.commit()


@pytest.fixture
def one_match(app):
    new_match1 = Match(
        user_id = MATCH_USER_ID1,
        match_name = MATCH_NAME1,
        no_of_sets = MATCH_NO_OF_SETS1,
        no_of_gamesperset = MATCH_NO_OF_GAMESPERSET1,
        playe_a_id = MATCH_PLAYER_A_ID1,
        playe_b_id = MATCH_PLAYER_B_ID1,
    )
    db.session.add(new_match1)
    db.session.commit()

@pytest.fixture
def second_match(app):
    new_match2 = Match(
        user_id = MATCH_USER_ID2,
        match_name = MATCH_NAME2,
        no_of_sets = MATCH_NO_OF_SETS2,
        no_of_gamesperset = MATCH_NO_OF_GAMESPERSET2,
        playe_a_id = MATCH_PLAYER_A_ID2,
        playe_b_id = MATCH_PLAYER_B_ID2,
    )
    db.session.add(new_match2)
    db.session.commit()




