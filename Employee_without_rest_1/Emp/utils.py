import json

def is_json(data):

    try:
        p_data=json.loads(data) #ensures that user is sending valid json data from parter application.
        valid=True
    except ValueError: #if its not json
        valid=False
    return valid
