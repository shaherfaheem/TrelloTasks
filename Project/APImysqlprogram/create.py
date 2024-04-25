import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import Flask, request, session
from fetchalltasks import fetchAllTasks


@app.route('/newtask', methods=['GET'])
def new_task():
   msg=''
   if 'loggedin' in session:

      return render_template("CreateNewTask.html")
   
   msg='log in your account'
   return render_template("Login.html",msg=msg)
   
   
@app.route('/taskcreated', methods=['POST'])
def home():
 msg=''
 try:
   cursor = mysql_db.cursor(dictionary=True)
   _task=request.form.get('task')
   _employee=request.form.get('employee')
   _status=request.form.get('status')
   _priority=request.form.get('priority')
   _startdate=request.form.get('startdate')
   _duration=request.form.get('duration')
   _deadline=request.form.get('deadline')

   
   if 'loggedin' in session:
      
      sql = "INSERT INTO tasks(task, employee, status, priority, startdate, duration, deadline) VALUES(%s, %s , %s, %s, %s , %s, %s)"
      data = (_task, _employee, _status, _priority, _startdate, _duration, _deadline )
   
      cursor.execute(sql, data)
      mysql_db.commit()
      msg='New Task Created!'
      return render_template('CreateNewTask.html',msg=msg)
   
   msg='log in your account'
   return render_template("Login.html",msg=msg)
 
 except Exception as e:
   print(e)
 finally:
   cursor.close() 
  

