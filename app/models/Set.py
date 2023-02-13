from app import db

class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_number = db.Column(db.Integer)
    player_a_gmaes_won = db.Column(db.Integer)
    player_b_gmaes_won = db.Column(db.Integer)
    match_id = db.Column(db.Integer, db.ForeignKey("match.id"), nullable=False)
    player_a_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player_b_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    players = db.relationship("Player", back_populates="set")
    games = db.relationship("Game", back_populates="set")
    match = db.relationship("Match",back_populates="set")

    def to_dict(self):
        set_dict = {}
        set_dict["id"] = self.id
        set_dict["set_number"] = self.set_number
        set_dict["player_a_gmaes_won"] = self.player_a_gmaes_won
        set_dict["player_b_gmaes_won"] = self.player_b_gmaes_won
        
        
        player_names = []
        for player in self.players:
            player_names.append(player.name)
        set_dict["player"] = player_names

        games_ids = []
        for game in self.games:
            games_ids.append(game.id)
        set_dict["match"] = games_ids
        return set_dict

    @classmethod
    def from_dict(cls, set_data):
        new_set = Set(set_number=set_data["set_number"],
                    player_a_gmaes_won=set_data["player_a_gmaes_won"],
                    player_b_gmaes_won=set_data["player_b_gmaes_won"],                    
                    registered_at = set_data["registered_at"],
                    player_names=set_data["player_names"],
                    games_ids=set_data["gmaes_ids"]
                    )
        return new_set
# id = pk
# set_number
# player_a_games_won
# player_b_games_won
# match_id = FK 