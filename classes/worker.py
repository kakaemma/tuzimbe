from utility.class_utility import json_response, \
    is_string, check_length, check_user_type, \
        check_time_stamp , check_integer, check_user_id
from utility.messages import Messages
from app.models import User, WorkDetails


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
            except Exception as exc:
                print (exc)         
        else:
            return json_response(valid_input_msg, 400)
        
    @classmethod
    def capture_wrk_details(cls, user_id, daily_rate,
                                arrival_time, departure_time): 
        
        valid_wrk_details_msg = cls.check_daily_work_details(
            user_id, daily_rate, arrival_time, departure_time) 
        if valid_wrk_details_msg == True:
            try:
                worker_name = User.check_user_exists_by_id(user_id)
                if worker_name:
                    WorkDetails.capture_details(user_id, daily_rate,
                                            arrival_time,departure_time)
                    message = Messages.work_details_added()
                    status_code = 201
                else:
                    message= Messages.worker_doesnt_exit()
                    status_code=400
                return json_response(message, status_code)
                
            except Exception as exc:
                print (exc)
        else:
            return json_response(valid_wrk_details_msg, 400)      
      
    @classmethod
    def validations(cls, name, user_type):

        valid_name = is_string(name)
        valid_user_type = check_user_type(user_type)
        valid_str_length = check_length(name)
        if not name or not user_type:
            response = Messages.missing_details()
        elif not valid_name:
            response = Messages.invalid_name()
        elif not valid_user_type:
            response = Messages.invalid_user_type()
        elif not valid_str_length:
            response = Messages.invalid_str_length()
        else:
            response = True
        return response
    
    @classmethod
    def check_daily_work_details(cls, user_id,daily_rate,
                                arrival_time, departure_time):
        user_id_present = check_user_id(user_id)
        is_valid_rate = check_integer(daily_rate)
        is_arrival_time_valid = check_time_stamp(arrival_time)
        is_departure_time_valid = check_time_stamp(departure_time)
        
        if not user_id_present:
            response = Messages.missing_user_id()
        elif not daily_rate or not arrival_time or not departure_time:
            response = Messages.missing_details()
        elif not is_valid_rate:
            response = Messages.invalid_rate()
        elif not is_arrival_time_valid:
            response = Messages.invalid_arrival_time()
        elif not is_departure_time_valid:
            response = Messages.invalid_departure_time()
        else:
            response =True
        return response
        