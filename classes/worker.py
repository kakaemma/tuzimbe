from utility.class_utility import json_response, \
    is_string, check_length, check_user_type 
from utility.messages import Messages
from app.models import User

class Worker(object):
    @classmethod
    def register_worker(cls, name, user_type):    
        valid_input_msg = cls.validations(name,user_type)
        if valid_input_msg == True:
            try:
                user_exists = User.check_if_user_exists(name)
                if user_exists:
                    message = Messages.user_exists()
                    status_code = 400
                else:
                    User.register_user(name, user_type)
                    message = Messages.successfully_added_user()
                    status_code = 200        
                return json_response(message,status_code)
            except:
                print ('failed to add user')         
        else:
            return json_response(valid_input_msg, 400)
    
    @classmethod
    def validations(cls, name, user_type):
        valid_name = is_string(name)
        valid_user_type = check_user_type(user_type)
        valid_str_length = check_length(name)
        if not valid_name:
            response = Messages.invalid_name()
        elif not valid_user_type:
            response = Messages.invalid_user_type()
        elif not valid_str_length:
            response = Messages.invalid_str_length()
        else:
            response = True
        return response
    