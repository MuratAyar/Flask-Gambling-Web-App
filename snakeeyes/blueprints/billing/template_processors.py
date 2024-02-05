import datetime
import pytz

from lib.money import cents_to_dollars


def format_currency(amount, convert_to_dollars=True):
    
    if convert_to_dollars:
        amount = cents_to_dollars(amount)

    return '{:,.2f}'.format(amount)


def current_year():
    
    return datetime.datetime.now(pytz.utc).year
