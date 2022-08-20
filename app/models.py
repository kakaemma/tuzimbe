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
    @staticmethod
    def check_user_exists_by_id(user_id):
        try:
            query_for_checking_user = "SELECT name FROM users WHERE id=%s"
            connection.cursor.execute(query_for_checking_user, [user_id])
            row = connection.cursor.fetchone()
            return row
        except Exception as ex:
            print(ex)

    
class WorkDetails(object):
    @staticmethod
    def capture_details(user_id, daily_rate,  arrival_time, departure_time):
        try:
            add_work_details = "INSERT INTO worker_details(user_id, daily_rate, \
            arrival_time,departure_time) VALUES (%s,%s,%s,%s,%s)"
            connection.cursor.execute(
            add_work_details, 
            (user_id, daily_rate,  arrival_time, departure_time))
        except Exception as exec:
            print(exec)
            
  