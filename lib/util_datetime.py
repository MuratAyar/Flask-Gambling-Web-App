import datetime
import pytz


def tzware_datetime():
    
    return datetime.datetime.now(pytz.utc)


def timedelta_months(months, compare_date=None):
    
    if compare_date is None:
        compare_date = datetime.date.today()

    delta = months * 365 / 12
    compare_date_with_delta = compare_date + datetime.timedelta(delta)

    return compare_date_with_delta
