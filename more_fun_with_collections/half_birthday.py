# Zachary Hayes
from datetime import datetime, timedelta


def half_birthday(birth_date):
    return birth_date + timedelta(6*365/12)
