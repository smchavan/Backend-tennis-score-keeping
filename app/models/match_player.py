from app import db
import datetime

class Match_player(db.Model):
    #id = db.Column(db.Integer, primary_key=True,nullable=False)

    match_id = db.Column(db.Integer, db.ForeignKey('match.id'),primary_key=True,  nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'),primary_key=True,  nullable=False)

    matches = db.relationship("Match", back_populates="match_players")
    players = db.relationship("Player", back_populates="match_players")

    def to_dict(self):
        match_player_dict = {}
        #match_player_dict["id"] = self.id
        match_player_dict["match_id"] = self.match_id
        match_player_dict["player_id"] = self.player_id
        
        return match_player_dict

    @classmethod
    def from_dict(cls, match_player_data):
        new_match_player = Match_player(
            match_id = match_player_data["match_id"],
            player_id = match_player_data["player_id"]
        )
        return new_match_player