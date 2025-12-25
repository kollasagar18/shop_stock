import mysql.connector
def db_con():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kollasagar@93",
    database="ration_shop"
)
