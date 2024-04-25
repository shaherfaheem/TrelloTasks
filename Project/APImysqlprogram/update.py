import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import Flask, request,session
from fetchalltasks import fetchAllTasks

@app.route('/taskupdate', methods=['POST'])
def updateTask():
 msg='' 
 try:
   cursor = mysql_db.cursor(dictionary=True)
   _id=request.form.get('id')
   _task=request.form.get('task')
   _employee=request.form.get('employee')
   _status=request.form.get('status')
   _priority=request.form.get('priority')
   _startdate=request.form.get('startdate')
   _duration=request.form.get('duration')
   _deadline=request.form.get('deadline' )
  
   if 'loggedin' in session:
     
     sql = "UPDATE tasks SET task=%s, employee=%s, status=%s, priority=%s, startdate=%s, duration=%s,deadline=%s WHERE id=%s"
     data = (_task, _employee, _status, _priority, _startdate, _duration, _deadline, _id)

     cursor.execute(sql, data)
     mysql_db.commit()
     msg= 'Task Updated!'
     return render_template('ProjectTasks.html',datas=fetchAllTasks(),msg=msg)
  
   msg='log in your account'
   return render_template("Login.html",msg=msg)

 except Exception as e:
  print(e)
 finally:
  cursor.close() 
