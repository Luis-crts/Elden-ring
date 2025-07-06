import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="database-3.ch0aakoqo1e3.us-east-1.rds.amazonaws.com",
        user="admin",
        password="asdfmovie",        
        database="eldenring",
        port=3306
    )
