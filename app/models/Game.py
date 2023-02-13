from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_number = db.Column(db.Integer) #Todo- add autoincrement
    player_a_score = db.Column(db.Integer)
    player_b_score = db.Column(db.Integer)
    set_id = db.Column(db.Integer, db.ForeignKey("set.id"), nullable=False)
    
    set = db.relationship("Set",back_populates="games")

    def to_dict(self):
        game_dict = {}
        game_dict["id"] = self.id
        game_dict["game_number"] = self.game_number
        game_dict["player_a_score"] = self.player_a_score
        game_dict["player_b_score"] = self.player_b_score
        
        return 

    @classmethod
    def from_dict(cls, game_data):
        new_game = Game(game_number=game_data["game_number"],
                    player_a_game_won=game_data["player_a_games_won"],
                    player_b_games_won=game_data["player_b_games_won"],                    
                    registered_at = game_data["registered_at"],
                    player_names=game_data["player_names"],
                    games_ids=game_data["games_ids"]
                    )
        return new_game