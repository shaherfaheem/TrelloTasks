import pymysql
from app import app
from mysql_db import mysql_db
import hashlib
import re
from employeeLogin import access
from employeeLogin import CreateAccount
from employeeLogin import NewAccount
from employeeLogin import Login
from employeeLogin import Logout
from create import new_task
from create import home
from lists import list_of_tasks
from lists import open_tasks
from lists import completed_tasks
from delete import deleteTask
from update import updateTask
from fetchalltasks import fetchAllTasks
from fetchopentasks import fetchListOfOpenTasks
from fetchCompleted import fetchCompletedTasks
from fetchaccs import fetchAccs
from completedtask import completed_task
from errorhandler import page_not_found
from flask import render_template
from flask import Flask, request, session


    


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
