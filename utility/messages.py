class Messages(object):
    @classmethod
    def invalid_name(cls):
        return {'error': 'Invalid name. string required'}
    
    @classmethod
    def missing_details(cls):
        return {'error': 'missing details in body'}
    
    @classmethod
    def missing_user_id(cls):
        return {'error': 'missing user_id in body'}
    
    @classmethod
    def invalid_str_length(cls):
        return {'error': 'Invalid name length. a minimum\
            lenghth of three characters is required'}
    
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
    def work_details_added(cls):
        return {'message': 'Work details successfully added'}
    
    @classmethod
    def invalid_rate(cls):
        return {'error': 'The daily rate is not valid'}
    @classmethod
    def invalid_arrival_time(cls):
        return {'error': 'The arrival time is not valid'}
    @classmethod
    def invalid_departure_time(cls):
        return {'error': 'Departure time is not valid '}
    
    @classmethod
    def worker_doesnt_exit(cls):
        return {'error': 'Worker does not exist'}
    
    @classmethod
    def invalid_material_type(cls):
        return {'error': 'Invalid material type, use sand, cement, bricks,nails,water, stone aggregates '}
    
    @classmethod
    def invalid_quantity(cls):
        return {'error': 'Quantity is not valid.'}
    
    @classmethod
    def invalid_price(cls):
        return {'error': 'Price is not valid'}     
    
    @classmethod
    def material_added(cls):
        return {'message': 'Materials details successfully added'}       
    
    @classmethod
    def invalid_keys(cls):
        return {'error':'Invalid keys submited'}
    