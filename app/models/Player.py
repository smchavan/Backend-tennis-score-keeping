from app import db
from app.models.match_player import Match_player
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.String, nullable=False)
    serve_style = db.Column(db.String, nullable=False)
    utr = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    user = db.relationship("User", back_populates="players")
    match_players = db.relationship("Match_player", back_populates="players")
    
    # stats = db.relationship("Stat",back_populates="player")
    
    def to_dict(self):
        player_dict = {}
        player_dict["id"] = self.id
        player_dict["first_name"] = self.first_name
        player_dict["last_name"] = self.last_name
        player_dict["date_of_birth"] = self.date_of_birth
        player_dict["serve_style"] = self.serve_style
        player_dict["utr"] = self.utr

        match_names = []
        for match in self.matches:
            match_names.append(match.name)
        player_dict["match"] = match_names

        return player_dict

    @classmethod
    def from_dict(cls, player_data):
        new_player = Player(
            first_name = player_data["first_name"],
            last_name = player_data["last_name"],
            date_of_birth = player_data["date_of_birth"],
            serve_style = player_data["serve_style"],
            utr = player_data["utr"]
        )
        return new_player