import sqlite3
from flask import Blueprint, render_template, request, make_response, redirect
from database.database import Database

home = Blueprint('homepage', __name__, )


@home.route('/homepage')
def homepage():
    return render_template("homepage.html")


@home.route('/home')
def hello_name():
    return render_template("home.html")
