import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import flash, request,session
from fetchalltasks import fetchAllTasks

@app.route('/completed', methods=['POST'])
def completed_task():
 msg=''
 try:
   cursor = mysql_db.cursor(dictionary=True)
   _id=request.form.get('id')
   print(_id)

   if 'loggedin' in session:
  
    sql = "UPDATE tasks SET status='Completed' WHERE id=%s"
    cursor.execute(sql,[_id])
    mysql_db.commit()
    msg='Task Status Updated!'
    return render_template('ProjectTasks.html',datas=fetchAllTasks(),msg=msg)
   
   msg='log in your account'
   return render_template("Login.html",msg=msg)
 except Exception as e:
  print(e)
 finally:
  cursor.close() 