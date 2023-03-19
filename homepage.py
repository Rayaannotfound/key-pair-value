import sqlite3
from flask import Blueprint, render_template, request, make_response, redirect
from database.database import Database

home = Blueprint('homepage', __name__, )


# returns the homepage page
@home.route('/homepage')
def homepage():
    return render_template("homepage.html")


# returns the login page
@home.route('/login')
def hello_name():
    return render_template("login.html")
