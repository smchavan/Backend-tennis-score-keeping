from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config["Testing"] = True
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    from app.models.user import User
    from app.models.player import Player
    from app.models.match import Match
    from app.models.set import Set
    from app.models.game import Game
    from app.models.stat import Stat
    from app.models.match_player import Match_player

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.user_routes import users_bp
    app.register_blueprint(users_bp)

    from app.routes.player_routes import players_bp
    app.register_blueprint(players_bp)

    from app.routes.match_routes import matchs_bp
    app.register_blueprint(matchs_bp)

    from app.routes.set_routes import sets_bp
    app.register_blueprint(sets_bp)

    from app.routes.game_routes import games_bp
    app.register_blueprint(games_bp)

    from app.routes.stat_routes import stats_bp
    app.register_blueprint(stats_bp)

    from app.routes.match_player_routes import match_players_bp
    app.register_blueprint(match_players_bp)

    CORS(app)
    return app
