import pymysql
from app import app
from mysql_db import mysql_db
from flask import render_template
from flask import flash, request


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")