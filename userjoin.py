import sqlite3
import re

from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from homepage import homepage
from database.database import Database

user_join = Blueprint('user_join', __name__, )
login_manager = LoginManager()
bcrypt = Bcrypt()


class userObj(UserMixin):
    def __init__(self, name):
        self.name = name
        self.id = name


@login_manager.unauthorized_handler
def handle_needs_login():
    return redirect(url_for('user_join.login', next=request.endpoint))


def init_flask_login(app):
    global bcrypt
    global login_manager
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.blueprint_login_views = {
        'user_join': '/login',
    }
    bcrypt = Bcrypt(app)


@login_manager.user_loader
def load_user(user_id):
    return userObj(user_id)


@user_join.route('/')
def new_user():
    return render_template('user.html')


@user_join.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        username = request.form['Username']
        password = request.form['Password']
        print ("[" + username + "]")
        results = Database.get_instance().run_query("""SELECT * FROM accounts WHERE username = (?)""", (username,))

        if results:
            account = results[0]
            if bcrypt.check_password_hash(account[1], password):
                login_user(userObj(account[0]))
                msg = 'Logged in successfully !'
            else:
                msg = 'Incorrect username / password combination!'
            return render_template('home.html', msg=msg)
        else:
            msg = 'Incorrect username / password combination !'
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
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            db.run_query('INSERT INTO accounts VALUES (?, ?)', (username, hashed_password, ))
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('signup.html', msg=msg)


@user_join.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_join.login'))