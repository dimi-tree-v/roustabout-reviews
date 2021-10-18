import uuid


def get_unique_id():
    return uuid.uuid1(16).hex
