from flask import redirect, url_for
from flask import Blueprint

user = Blueprint('users', __name__, )


@user.route('/admin')
def admin():
    return 'Hello System Admin'


@user.route('/guest/<guest>')
def authguest(guest):
    return 'Hello %s as Guest' % guest


@user.route('/user/<name>')
def username(name):
    if name == 'admin':
        return redirect(url_for('users.admin'))
    else:
        return redirect(url_for('users.authguest', guest=name))
