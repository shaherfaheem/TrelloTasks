import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import flash, request


def fetchCompletedTasks():
 try:
   cursor = mysql_db.cursor(dictionary=True)
  
   cursor.execute("SELECT * FROM tasks Where status = 'Completed'")
   rows = cursor.fetchall()
   return rows
 except Exception as e:
   print(e)
 finally:
   cursor.close() 
