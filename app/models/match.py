from app import db
import datetime
from app.models.match_player import Match_player
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_of_sets = db.Column(db.Integer)
    no_of_gamesperset = db.Column(db.Integer)
    match_date = db.Column(db.DateTime, default=(datetime.date.today()))
    match_name = db.Column(db.String)
    match_winner = db.Column(db.String)
    player_a_sets_won = db.Column(db.Integer)
    player_b_sets_won = db.Column(db.Integer)
    player_a_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False) # Make sure they are Unique in player id
    player_b_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    match_players = db.relationship("Match_player", back_populates="matches")

    user = db.relationship("User", back_populates="matches")
    sets = db.relationship("Set",back_populates="match")

    # player_a = db.relationship(
    #     "Player",
    #     foreign_keys="Match.player_a_id",
    #     back_populates="match1"
    # )

    # player_b = db.relationship(
    #     "Player",
    #     foreign_keys="Match.player_b_id",
    #     back_populates="match2"
    # )
    
    def to_dict(self):
        match_dict = {}
        match_dict["id"] = self.id
        match_dict["no_of_sets"] = self.no_of_sets
        match_dict["no_of_gamesperset"] = self.no_of_gamesperset
        match_dict["match_date"] = self.match_date
        match_dict["match_name"]= self.match_name
        match_dict["player_a_id"]= self.player_a_id
        match_dict["player_b_id"]= self.player_b_id
        match_dict["user_id"]= self.user_id
        match_dict["player_a_sets_won"] = self.player_a_sets_won
        match_dict["player_b_sets_won"] = self.player_b_sets_won
        match_dict["match_winner"] = self.match_winner
        #player_names = []
        # for player in self.players:
        #     player_names.append(player.first_name)
        # match_dict["player"] = player_names
        
        return match_dict

        
    @classmethod
    def from_dict(cls, match_data):
        new_match = Match(no_of_sets=match_data["no_of_sets"],
                    no_of_gamesperset=match_data["no_of_gamesperset"],
                    player_a_id=match_data["player_a_id"],
                    player_b_id=match_data["player_b_id"],
                    match_date = match_data["match_date"],
                    match_name=match_data["match_name"],
                    match_winner=match_data["match_winner"],
                    player_a_sets_won=match_data["player_a_sets_won"],
                    player_b_sets_won=match_data["player_b_sets_won"]                     
                    )
        return new_match
