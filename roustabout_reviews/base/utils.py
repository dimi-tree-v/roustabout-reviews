import uuid


def get_unique_id():
    return uuid.uuid1(16).hex

def get_average(array, decimal_places=2):
    if not array:
        return None
        
    average = sum(array)/len(array)
    return round(average, decimal_places)
