import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import Flask, request, session
from fetchalltasks import fetchAllTasks
from fetchopentasks import fetchListOfOpenTasks
from fetchCompleted import fetchCompletedTasks



@app.route('/alltasks', methods=['GET'])
def list_of_tasks():
   msg=''
   if 'loggedin' in session:
  
      return render_template('ProjectTasks.html',datas=fetchAllTasks())
   
   msg='log in your account'
   return render_template("Login.html",msg=msg)

@app.route('/opentasks', methods=['GET'])
def open_tasks():
   msg=''
   if 'loggedin' in session:
  
      return render_template('ProjectTasks.html',datas=fetchListOfOpenTasks())
   
   msg='log in your account'
   return render_template("Login.html",msg=msg)


@app.route('/completedTasks', methods=['GET'])
def completed_tasks():
   msg=''
   if 'loggedin' in session:

      return render_template('ProjectTasks.html',datas=fetchCompletedTasks())
   
   msg='log in your account'
   return render_template("Login.html",msg=msg)