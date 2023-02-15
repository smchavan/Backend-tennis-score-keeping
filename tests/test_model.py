from app.models.user import User
from app.models.player import Player
from app.models.match import Match
from app.models.set import Set
from app.models.game import Game
from app.models.stat import Stat
from app.models.match_player import Match_player
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

# TEST for to_dict of User Model
def test_to_dict_no_missing_data():
    # Arrange
    new_user2 = User(
        id = 1,
        first_name = USER_FIRST_NAME2,
        last_name = USER_LAST_NAME2,
        email = USER_EMAIL2,
        password = USER_PASSWORD2,
        registered_at = "sadsadsad"
    )
    # Act
    result = new_user2.to_dict()
    # Assert
    assert len(result) == 8
    assert result["id"] == 1
    assert result["first_name"] == " First NAme of TEST User2"
    assert result["last_name"] == "Last Name Of Test User2"
    assert result["email"] == "ppppppppp"
    assert result["password"] == "qqqqqqqqqq"
    assert result["registered_at"] == "sadsadsad"

## Test for form_dict for User Model
def test_from_dict_returns_planet():
    # Arrange
    new_user2 = {
        "id": 1,
        "first_name" : USER_FIRST_NAME2,
        "last_name":USER_LAST_NAME2,
        "email":USER_EMAIL2,
        "password": USER_PASSWORD2,
        "registered_at":"sadsadsad"
        
    }
    # Act
    result = User.from_dict(new_user2)
    # Assert
    assert result.first_name == " First NAme of TEST User2"
    assert result.last_name == "Last Name Of Test User2"
    assert result.email == "ppppppppp"
    assert result.password == "qqqqqqqqqq"
    assert result.registered_at == "sadsadsad"
