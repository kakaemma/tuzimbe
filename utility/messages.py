class Messages(object):
    @classmethod
    def invalid_name(cls):
        return {'error': 'Invalid name. string required'}
    
    @classmethod
    def invalid_str_length(cls):
        return {'error': 'Invalid name length. a minimum lenghth of three characters is required'}
    
    @classmethod
    def invalid_user_type(cls):
        return {'error': 'Invalid user_type. user worker or owner'}
    
    
    @classmethod
    def successfully_added_user(cls):
        return {'message': 'User has been successfully added'}
    
    @classmethod
    def user_exists(cls):
        return {'error': 'User already exists in the system'}
    
    @classmethod
    def content_type(cls):
        return {'error': 'ContentType  should be application/json'}
    
    @classmethod
    def invalid_keys(cls):
        return {'error':'Invalid keys submited'}