import datetime
import re
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

def check_time_stamp(time_stamp):
    
    timestamp_regex=r'([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9])'
    valid_time_stmp = bool(re.match(timestamp_regex, time_stamp))
    if valid_time_stmp:
        return True
    return False    

def check_rate(daily_rate):
    if daily_rate and type(daily_rate)== int:
        return True
    return False

    
def invalid_keys():
    return json_response(Messages.invalid_keys, 400)

   