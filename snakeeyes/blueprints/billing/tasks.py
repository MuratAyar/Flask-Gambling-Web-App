from snakeeyes.app import create_celery_app
from snakeeyes.blueprints.user.models import User
from snakeeyes.blueprints.billing.models.credit_card import CreditCard
from snakeeyes.blueprints.billing.models.coupon import Coupon

celery = create_celery_app()


@celery.task()
def mark_old_credit_cards():
    
    return CreditCard.mark_old_credit_cards()


@celery.task()
def expire_old_coupons():
    
    return Coupon.expire_old_coupons()


@celery.task()
def delete_users(ids):

    return User.bulk_delete(ids)


@celery.task()
def delete_coupons(ids):
    """
    Delete coupons both on the payment gateway and locally.

    :param ids: List of ids to be deleted
    :type ids: list
    :return: int
    """
    return Coupon.bulk_delete(ids)
