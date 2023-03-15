from flask import Blueprint, render_template, request, session
from homepage import homepage
import sqlite3
import re

user = Blueprint('userjoin', __name__, )


@user.route('/')
def newuser():
    return render_template('user.html')


@user.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        username = request.form['Username']
        password = request.form['Password']
        connect = sqlite3.connect('flashcard.db')
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM accounts WHERE username = (?) AND password = (?)""", (username, password))
        account = cursor.fetchone()
        if account:
            msg = 'Logged in successfully !'
            return render_template('home.html', msg=msg)
        else:
            msg = 'Incorrect username / password combination!'
    return render_template('home.html', msg=msg)


@user.route('/signup', methods=['POST', 'GET'])
def signup():
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        username = request.form['Username']
        password = request.form['Password']
        connect = sqlite3.connect('flashcard.db')
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM accounts WHERE username = (?)""", (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, ?, ?)', (username, password, ))
            connect.commit()
            connect.close()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('signup.html', msg=msg)



