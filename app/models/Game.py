from app import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_number = db.Column(db.Integer) #Todo- add autoincrement
    player_a_score = db.Column(db.Integer,default=0)
    player_b_score = db.Column(db.Integer,default=0)
    set_id = db.Column(db.Integer, db.ForeignKey("set.id"), nullable=False)
    
    set = db.relationship("Set",back_populates="games")

    def to_dict(self):
        game_dict = {}
        game_dict["id"] = self.id
        game_dict["game_number"] = self.game_number
        game_dict["player_a_score"] = self.player_a_score
        game_dict["player_b_score"] = self.player_b_score
        game_dict["set_id"] = self.set_id
        
        return game_dict

    @classmethod
    def from_dict(cls, game_data):
        new_game = Game(game_number=game_data["game_number"],
                    player_a_score=game_data["player_a_score"],
                    player_b_score=game_data["player_b_score"],                    
                    set_id=game_data["set_id"]
                    )
        return new_game
    




