import sqlite3
import re

from flask import Blueprint, render_template, request, session, redirect, url_for
# all of these imports are for logging in
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# used for encryption
from flask_bcrypt import Bcrypt
from homepage import homepage
from database.database import Database

user_join = Blueprint('user_join', __name__, )
login_manager = LoginManager()
bcrypt = Bcrypt()


class userObj(UserMixin):  # instance of the account values to use
    def __init__(self, name):
        self.name = name
        self.id = name


@login_manager.unauthorized_handler
def handle_needs_login():
    return redirect(url_for('user_join.login', next=request.endpoint))


# handles any unauthorized logging in

def init_flask_login(app):
    global bcrypt  # encryption
    global login_manager  # logging in safely
    login_manager.init_app(app)  # internal flask method
    login_manager.login_view = "login"
    login_manager.blueprint_login_views = {
        'user_join': '/login',
    }
    bcrypt = Bcrypt(app)


@login_manager.user_loader
def load_user(user_id):
    return userObj(user_id)


@user_join.route('/')  # defines the page where a user is prompted to sign up or log in
def new_user():
    return render_template('user.html')


@user_join.route('/login', methods=['POST', 'GET'])
def login():
    # takes in the values from the form
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        username = request.form['Username']
        password = request.form['Password']
        print("[" + username + "]")
        results = Database.get_instance().run_query("""SELECT * FROM accounts WHERE username = (?)""", (username,))

        # account details are checked against the database
        if results:
            account = results[0]
            # bcrypt checks the password which
            # has been encrypted against your input and lets you log in if successful
            if bcrypt.check_password_hash(account[1], password):
                login_user(userObj(account[0]))
                msg = 'Logged in successfully !'
                return render_template('homepage.html', msg=msg)
            else:
                msg = 'Incorrect username / password combination!'
            return render_template('login.html', msg=msg)
        else:
            msg = 'Incorrect username / password combination !'
    return render_template('login.html', msg=msg)  # login page gets sent to the user with this logic


@user_join.route('/signup', methods=['POST', 'GET'])
def signup():
    # takes in user input for signing up
    msg = ''
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        username = request.form['Username']
        password = request.form['Password']
        db = Database.get_instance()
        # compares information to accounts to check for duplicates
        results = db.run_query("""SELECT * FROM accounts WHERE username = (?)""", (username,))
        if results:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        # encrypts the password for storing
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            db.run_query('INSERT INTO accounts VALUES (?, ?)', (username, hashed_password,))
            msg = 'You have successfully registered!'
    # handles no input but sent data
    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('signup.html', msg=msg)  # page for signing up


@user_join.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_join.login'))  # logs a user out, stopping session and denying access to pages
