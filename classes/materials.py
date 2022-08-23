from utility.class_utility import json_response, check_material_type,check_integer
from utility.messages import Messages
from app.models import MaterialDetails


class Materials(object):
    
    @classmethod
    def add_materials(cls, material_type, quantity, unit_price):
        
        validation_msg = cls.validate_materials(material_type,quantity,unit_price)
        if validation_msg == True:
            MaterialDetails.capture_material_details(material_type, quantity, unit_price)
            response = Messages.material_added()
            return json_response(response, 201)
        else:
            return json_response(validation_msg, 400)    
    
    @classmethod 
    def validate_materials(cls, material_type, quantity, unit_price):
        
        if material_type and quantity and unit_price:
            is_material_valid = check_material_type(material_type)
            is_quantity_valid = check_integer(quantity)
            is_unit_price_valid= check_integer(unit_price)
            
            if not is_material_valid:
                response = Messages.invalid_material_type()
            elif not is_quantity_valid:
                response = Messages.invalid_quantity()
            elif not is_unit_price_valid:
                response = Messages.invalid_price()
            else:
                response = True
        else:
            response = Messages.missing_details()
        return response
    