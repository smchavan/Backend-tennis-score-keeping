from app import db

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_number = db.Column(db.Integer) # Should be incremented everytime new set starts
    player_a_games_won = db.Column(db.Integer,default=0)
    player_b_games_won = db.Column(db.Integer,default=0)
    set_winner = db.Column(db.String)
    set_done = db.Column(db.Boolean,default = False)
    match_id = db.Column(db.Integer, db.ForeignKey("match.id"), nullable=False)
    
    stats = db.relationship("Stat",back_populates="set")
    games = db.relationship("Game", back_populates="set")
    match = db.relationship("Match",back_populates="sets")

    def to_dict(self):
        set_dict = {}
        set_dict["id"] = self.id
        set_dict["set_number"] = self.set_number
        set_dict["player_a_games_won"] = self.player_a_games_won
        set_dict["player_b_games_won"] = self.player_b_games_won
        set_dict["match_id"] = self.match_id
        set_dict["set_winner"] = self.set_winner
        return set_dict


    @classmethod
    def from_dict(cls, set_data):
        new_set = Set(set_number=set_data["set_number"],
                    player_a_games_won=set_data["player_a_games_won"],
                    player_b_games_won=set_data["player_b_games_won"],                    
                    set_winner=set_data["set_winner"],
                    match_id=set_data["match_id"]
                    )
        return new_set
