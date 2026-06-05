import mysql.connector
import os

def db_con():
    return mysql.connector.connect(
        host=os.getenv("mysql.railway.internal"),
        user=os.getenv("root"),
        password=os.getenv("IQThGwvASQrDbFnqXkJsGWOzEfBBJXsH"),
        database=os.getenv("railway"),
        port=os.getenv("3306")
    )