from lib.util_sqlalchemy import ResourceMixin
from lib.util_datetime import tzware_datetime
from snakeeyes.extensions import db


class Bet(ResourceMixin, db.Model):
    __tablename__ = 'bets'
    id = db.Column(db.Integer, primary_key=True)

    # Relationships.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                        index=True, nullable=False)

    # Bet details.
    guess = db.Column(db.Integer())
    die_1 = db.Column(db.Integer())
    die_2 = db.Column(db.Integer())
    roll = db.Column(db.Integer())
    wagered = db.Column(db.BigInteger())
    payout = db.Column(db.Float())
    net = db.Column(db.BigInteger())

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Bet, self).__init__(**kwargs)

    @classmethod
    def is_winner(cls, guess, roll):
        
        if guess == roll:
            return True

        return False

    @classmethod
    def determine_payout(cls, payout, is_winner):
        
        if is_winner:
            return payout

        return 1.0

    @classmethod
    def calculate_net(cls, wagered, payout, is_winner):
        
        if is_winner:
            return int(wagered * payout)

        return -wagered

    def save_and_update_user(self, user):
        
        self.save()

        user.coins += self.net
        user.last_bet_on = tzware_datetime()
        return user.save()

    def to_json(self):
        
        params = {
          'guess': self.guess,
          'die_1': self.die_1,
          'die_2': self.die_2,
          'roll': self.roll,
          'wagered': self.wagered,
          'payout': self.payout,
          'net': self.net,
          'is_winner': Bet.is_winner(self.guess, self.roll)
        }

        return params
