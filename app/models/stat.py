from app import db
import datetime

class Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aces = db.Column(db.Integer)
    winners = db.Column(db.Integer)
    double_faults = db.Column(db.Integer)
    unforced_errors = db.Column(db.Integer)
    forced_errors = db.Column(db.Integer)
    
    set_id = db.Column(db.Integer, db.ForeignKey("set.id"), nullable=False)
    player_a_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player_b_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)

    players = db.relationship("Player", back_populates="stats")
    set = db.relationship("User",back_populates="stats")

    def to_dict(self):
        stat_dict = {}
        stat_dict["id"] = self.id
        stat_dict["set_id"] = self.set_id
        stat_dict["aces"] = self.aces
        stat_dict["winners"] = self.winners
        stat_dict["double_faults"] = self.double_faults
        stat_dict["unforced_errors"]: self.unforced_errors
        stat_dict["forced_errors"]: self.forced_errors
        stat_dict["player_a_id"]: self.player_a_id
        stat_dict["player_b_id"]: self.player_b_id

        player_names = []
        for player in self.players:
            player_names.append(player.first_name)
        stat_dict["player"] = player_names

        
    @classmethod
    def from_dict(cls, stat_data):
        new_stat = Stat(aces=stat_data["aces"],
                    winners=stat_data["winners"],
                    double_faults = stat_data["double_faults"],
                    unforced_errors=stat_data["unforced_errors"],
                    forced_errors=stat_data["forced_errors"],
                    player_a_id=stat_data["player_a_id"],
                    player_b_id=stat_data["player_b_id"],                    
                    player_names=stat_data["player_names"]
                    
                    )
        return new_stat