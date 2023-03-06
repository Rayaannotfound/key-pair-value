

from flask import Blueprint, render_template, request, make_response
from handlers.name_handler import name_handler;

flash = Blueprint('flashrouters', __name__,)

# A decorator used to tell the application
# which URL is associated function
# @app.route('/')
# def hello():
#    return 'Hi everyone its markiplier here'

# routing the decorator function hello_name
@flash.route('/home')
def hello_name():
    return render_template("home.html")


@flash.route('/flash/<question>')
def show_card( question):
    return 'Question: %s' % question

@flash.route('/flash/answer/<answer>')
def show_answers( answer):
    return 'Answer is %s' % answer

@flash.route('/flash')
def home():
    return 'flash cards'

@flash.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method=='POST':
        user = request.form['username']

    resp = make_response(render_template('cookie.html'))
    resp.set_cookie('userID', user)
    return resp

@flash.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome '+name+'</h1>'