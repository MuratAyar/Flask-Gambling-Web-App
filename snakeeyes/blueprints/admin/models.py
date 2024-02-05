from sqlalchemy import func

from snakeeyes.blueprints.user.models import db, User
from snakeeyes.blueprints.billing.models.subscription import Subscription
from snakeeyes.blueprints.bet.models.bet import Bet


class Dashboard(object):
    @classmethod
    def group_and_count_users(cls):
        
        return Dashboard._group_and_count(User, User.role)

    @classmethod
    def group_and_count_plans(cls):
        
        return Dashboard._group_and_count(Subscription, Subscription.plan)

    @classmethod
    def group_and_count_coupons(cls):
        
        not_null = db.session.query(Subscription).filter(
            Subscription.coupon.isnot(None)).count()
        total = db.session.query(func.count(Subscription.id)).scalar()

        if total == 0:
            percent = 0
        else:
            percent = round((not_null / float(total)) * 100, 1)

        return not_null, total, percent

    @classmethod
    def group_and_count_payouts(cls):
        
        return Dashboard._group_and_count(Bet, Bet.payout)

    @classmethod
    def _group_and_count(cls, model, field):
    
        count = func.count(field)
        query = db.session.query(count, field).group_by(field).all()

        results = {
            'query': query,
            'total': model.query.count()
        }

        return results
