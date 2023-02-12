from app import db
import datetime

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_of_sets = db.Column(db.Integer)
    no_of_gamesperset = db.Column(db.Integer)
    match_date = db.Column(db.DateTime, default=(datetime.date.today()))
    match_name = db.Column(db.String)
    player_a_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player_a_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    players = db.relationship("Player", back_populates="matches")
    user = db.relationship("User",back_populates="matches")

    def to_dict(self):
        match_dict = {}
        match_dict["id"] = self.id
        match_dict["no_of_sets"] = self.no_of_sets
        match_dict["no_of_gamesperset"] = self.no_of_gamesperset
        match_dict["match_date"] = self.match_date
        match_dict["match_name"]: self.match_name
        match_dict["player_a_id"]: self.player_a_id
        match_dict["player_b_id"]: self.player_b_id
        player_names = []
        for player in self.players:
            player_names.append(player.name)
        match_dict["player"] = player_names

        
    @classmethod
    def from_dict(cls, match_data):
        new_match = Match(no_of_sets=match_data["no_of_sets"],
                    no_of_gamesperset=match_data["no_of_gamesperset"],
                    player_a_id=match_data["player_a_id"],
                    player_b_id=match_data["player_b_id"],
                    match_date = match_data["match_date"],
                    match_name=match_data["match_name"],
                    player_names=match_data["player_names"]
                    
                    )
        return new_match