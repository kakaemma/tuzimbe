from email import message
from flask import jsonify
from utility.messages import Messages

def json_response(response, status_code=200):
    status_code = status_code
    return jsonify(response),status_code

def is_string(attribute):
    try:
        return attribute.encode('ascii').isalpha()
    except:
        return False
    
def check_length(name):
    if len(name) >= 3:
        return True
    return False

def check_user_type(user_type):
    user_types =['worker', 'owner']
    if user_type in user_types:
        return True
    return False
    
def invalid_keys():
    return json_response(Messages.invalid_keys, 400)

   