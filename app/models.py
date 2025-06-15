import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",         # si tienes contraseña, colócala aquí
        database="eldenring",
        port=3306
    )
