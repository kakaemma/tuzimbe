from functools import wraps
from flask import request,jsonify
from utility.class_utility import json_response

from utility.messages import Messages


def select_method_to_return(function, *args, **kwargs):
    try:
        if len(args) == 0 and len(kwargs)==0:
            return function()
        else:
            return function(*args, **kwargs)

    except Exception as exc:
        return jsonify({
            "error":exc
        })
        
def validate_content_type(func):

    @wraps(func)
    def decorated_method(*args, **kwargs):
        if request.headers.get('content-type') != 'application/json':
            response = Messages.content_type()
            status_code = 400
            return json_response(response, status_code)
        return select_method_to_return(func, *args, **kwargs)
    return decorated_method