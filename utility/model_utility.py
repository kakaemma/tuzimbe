import datetime
from app.views import registe_user
from database import DatabaseConnection

connection = DatabaseConnection()



class UserModel(object):
    
    @staticmethod
    def register_user(name, user_type):
        
        registe_user_query ="INSER INTO  users(name,user_type) VALUES(%s,%s)"
        connection.cursor.execute(registe_user_query,(name, user_type))
        