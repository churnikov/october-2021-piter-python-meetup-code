from random import random

from app.errors import DataExistsError


def add_data_to_db(data: dict):
    if round(random()):
        raise DataExistsError()
