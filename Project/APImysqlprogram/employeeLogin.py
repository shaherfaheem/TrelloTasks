
import hashlib
import re
import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import Flask, request, session
from fetchalltasks import fetchAllTasks


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