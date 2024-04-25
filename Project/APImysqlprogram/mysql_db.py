from app import app
import mysql.connector

# MySQL configuration
mysql_db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root123",
    database="databasetest"
)