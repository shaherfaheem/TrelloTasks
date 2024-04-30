from datetime import datetime
# from employeeLogin import access
# from employeeLogin import CreateAccount
# from employeeLogin import NewAccount
# from employeeLogin import Login
# from employeeLogin import Logout
# from create import new_task
# from create import home
# from lists import list_of_tasks
# from lists import open_tasks
# from lists import completed_tasks
# from delete import deleteTask
# from update import updateTask
# from fetchalltasks import fetchAllTasks
# from fetchopentasks import fetchListOfOpenTasks
# from fetchCompleted import fetchCompletedTasks
# from fetchaccs import fetchAccs
# from completedtask import completed_task
# from errorhandler import page_not_found
import hashlib
import re
from flask import render_template
from flask import Flask, request, session
# from app import app
import mysql.connector

app = Flask(__name__)

app.secret_key = 'my accounts key'

# MySQL configuration
mysql_db = mysql.connector.connect(
    host="host.docker.internal",
    port="3306",
    user="root",
    password="root123",
    database="databasetest"
)





def fetchAllTasks():

  try:
    cursor = mysql_db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    
    return rows
  except Exception as e:
    print(e)
  finally:
    cursor.close() 




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


   


def fetchListOfOpenTasks():
 try:
   cursor = mysql_db.cursor(dictionary=True)
  
   cursor.execute("SELECT * FROM tasks Where status != 'Completed'")
   rows = cursor.fetchall()
   return rows
 except Exception as e:
   print(e)
 finally:
   cursor.close() 


   


def fetchAccs():
 try:
   cursor = mysql_db.cursor(dictionary=True)
  
   cursor.execute("SELECT * FROM accounts")
   rows = cursor.fetchall()
   return rows
 except Exception as e:
   print(e)
 finally:
   cursor.close() 



  


@app.route('/', methods=['GET'])
def Login():
   return render_template("Login.html")



@app.route('/login', methods=['GET','POST'])
def access():
 msg= ''
 try: 
    cursor = mysql_db.cursor(dictionary=True)
    _uname=request.form.get('uname')
    _pword=request.form.get('pword')
    
   
    hash = _pword + app.secret_key
    hash = hashlib.sha1(hash.encode())
    _pword = hash.hexdigest()
  
 
    cursor.execute("SELECT * FROM accounts WHERE uname = %s AND pword = %s",(_uname, _pword))
    account = cursor.fetchone()

    if account:

        session['loggedin'] = True
        session['id'] = account['id']
        session['uname'] = account['uname']

        msg = 'Login Successful!'
        return render_template('ProjectTasks.html',datas=fetchAllTasks(),msg=msg)
    
    else: 
        msg = 'Incorrect Username/Password!'    
        return render_template('Login.html',msg=msg)

 except Exception as e:
   print(e)
 finally:
   cursor.close() 
  

@app.route('/register', methods=['GET'])
def CreateAccount():
   return render_template("CreateAccount.html")


@app.route('/registration', methods=['GET','POST'])
def NewAccount():
 
 msg= ''
 try:
   cursor = mysql_db.cursor(dictionary=True)
  
   _uname=request.form.get('uname')
   _email=request.form.get('email')
   _pword=request.form.get('pword')
   _vpword=request.form.get('vpword')
   print(_uname,_email)

   cursor.execute("SELECT * FROM accounts WHERE uname = %s", [_uname])
   name = cursor.fetchone()
   cursor.execute("SELECT * FROM accounts WHERE email = %s", [_email])
   mail = cursor.fetchone()
   if name:
            msg='username already exists!'
            return render_template('CreateAccount.html',msg=msg)
   elif mail:
            msg='email already exists!'
            return render_template('CreateAccount.html',msg=msg)         
   elif not re.match(r'[^@]+@[^@]+\.[^@]+', _email):
            msg = 'Invalid email address!'
            return render_template('CreateAccount.html',msg=msg)
   elif not re.match(r'[A-Za-z0-9]+', _uname):
            msg = 'Username must contain only characters and numbers!'
            return render_template('CreateAccount.html',msg=msg)
   elif _pword != _vpword:
            msg='Passwords did not match!'
            return render_template('CreateAccount.html',msg=msg)
   else:

            hash = _pword + app.secret_key
            hash = hashlib.sha1(hash.encode())
            _pword = hash.hexdigest()
   
      
            cursor.execute("INSERT INTO accounts(uname, email, pword) VALUES(%s, %s , %s)",(_uname, _email, _pword))
            mysql_db.commit()
            msg='Account Creation Successful!'
   return render_template('Login.html',msg=msg)
 except Exception as e:
   print(e)
 finally:
   cursor.close() 
  

@app.route('/logout')
def Logout():
    
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
  
   return render_template('Login.html')






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




@app.route('/deleteEmployee', methods=['POST'])
def deleteTask():
 msg=''
 try:
   cursor = mysql_db.cursor(dictionary=True)
   _id=request.form.get('id')
   print(_id)
   
   if 'loggedin' in session:
    
    cursor.execute("DELETE FROM tasks WHERE id=%s", [_id])
    mysql_db.commit()
    msg='Successfully Deleted Task!'
    return render_template('ProjectTasks.html',datas=fetchAllTasks(),msg=msg)
   
   msg='log in your account'
   return render_template("Login.html",msg=msg)
 
 except Exception as e:
  print(e)
 finally:
  cursor.close() 





@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")


    


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
