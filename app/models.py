from sqlite3 import connect
from database import DatabaseConnection

connection = DatabaseConnection()

class User(object):
    @staticmethod
    def register_user(name, user_type):
        register_user_query = "INSERT INTO users(name, user_type) VALUES (%s,%s)"
        connection.cursor.execute(register_user_query,(name,user_type))
        
    @staticmethod
    def check_if_user_exists(name):
        query_for_checking_user = "SELECT name FROM users WHERE name=%s"
        connection.cursor.execute(query_for_checking_user, [name])
        row = connection.cursor.fetchone()
        return row
    