from flask import Blueprint, render_template, request, session
from homepage import homepage
import sqlite3
import re
from database.database import Database

user_join = Blueprint('user_join', __name__, )


@user_join.route('/')
def new_user():
    return render_template('user.html')


@user_join.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        username = request.form['Username']
        password = request.form['Password']
        results = Database.get_instance().run_query("""SELECT * FROM accounts WHERE username = (?) AND password = (?)""", (username, password))

        if results:
            msg = 'Logged in successfully !'
            return render_template('home.html', msg=msg)
        else:
            msg = 'Incorrect user_name / password combination!'
    return render_template('home.html', msg=msg)


@user_join.route('/signup', methods=['POST', 'GET'])
def signup():
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        username = request.form['Username']
        password = request.form['Password']
        db = Database.get_instance()
        results = db.run_query("""SELECT * FROM accounts WHERE username = (?)""", (username,))

        if results:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        else:
            db.run_query('INSERT INTO accounts VALUES (?, ?)', (username, password, ))
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('signup.html', msg=msg)
