from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_number = db.Column(db.Integer) #Todo- add autoincrement
    player_a_score = db.Column(db.Integer,default=0)
    player_b_score = db.Column(db.Integer,default=0)
    game_winner = db.Column(db.String)
    set_id = db.Column(db.Integer, db.ForeignKey("set.id"), nullable=False)
    
    set = db.relationship("Set",back_populates="games")

    def to_dict(self):
        game_dict = {}
        game_dict["id"] = self.id
        game_dict["game_number"] = self.game_number
        game_dict["player_a_score"] = self.player_a_score
        game_dict["player_b_score"] = self.player_b_score
        game_dict["set_id"] = self.set_id
        game_dict["game_winner"] = self.game_winner
        return game_dict

    @classmethod
    def from_dict(cls, game_data):
        new_game = Game(game_number=game_data["game_number"],
                    player_a_score=game_data["player_a_score"],
                    player_b_score=game_data["player_b_score"],                    
                    set_id=game_data["set_id"],
                    game_winner = game_data["game_winner"]
                    )
        return new_game
    




