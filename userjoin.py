from flask import Blueprint, render_template, request, make_response
import sqlite3

user = Blueprint('userjoin', __name__, )

@user.route('/')
def newuser():
    return render_template('user.html')

@user.route('/signup')
def signup():
    return render_template('signup.html')

