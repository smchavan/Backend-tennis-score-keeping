from app import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    registered_at = db.Column(db.DateTime, default=(datetime.date.today()))
    
    players = db.relationship("Player", back_populates="user")
    matches = db.relationship("Match",back_populates="user")

    def to_dict(self):
        user_dict = {}
        user_dict["id"] = self.id
        user_dict["first_name"] = self.first_name
        user_dict["last_name"] = self.last_name
        user_dict["email"] = self.email
        user_dict["password"] = self.password
        user_dict["registered_at"]= self.registered_at

        player_names = []
        for player in self.players:
            player_names.append(player.first_name)
        user_dict["player"] = player_names

        match_names = []
        for match in self.matches:
            match_names.append(match.match_name)
        user_dict["match"] = match_names
        return user_dict

    @classmethod
    def from_dict(cls, user_data):
        new_user = User(first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                    email=user_data["email"],
                    password=user_data["password"],
                    registered_at = user_data["registered_at"]
                    )
        return new_user
