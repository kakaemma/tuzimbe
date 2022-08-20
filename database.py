import os
import  psycopg2
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) 


class DatabaseConnection():
    def __init__(self):
        self.connection =psycopg2.connect( host=os.environ.get("HOST"), 
                                          database =os.environ.get("DATABASE_NAME"),
                                          user=os.environ.get("DB_USER"),
                                          password=os.environ.get("PASSWORD"), 
                                          port=os.environ.get("PORT"))
        self.connection.autocommit=True
        self.cursor = self.connection.cursor()
        
    def create_tables(self):
        creater_users_table_querry = (""" CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,
                                      name VARCHAR(20) NOT NULL, user_type VARCHAR(10));
                                      """)
        create_work_details_table = (""" CREATE TABLE IF NOT EXISTS 
                                worker_details(id SERIAL PRIMARY KEY,
                                user_id INTEGER NOT NULL,  
                                daily_rate VARCHAR (10) NOT NULL ,
                                arrival_time TIMESTAMP NOT NULL, 
                                departure_time TIMESTAMP NOT NULL ,
                                FOREIGN KEY (user_id)REFERENCES 
                                users (id));""")
        self.cursor.execute(creater_users_table_querry)
        self.cursor.execute(create_work_details_table)

        
