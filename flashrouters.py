

from flask import Blueprint, render_template, request, make_response


flash = Blueprint('flashrouters', __name__,)

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