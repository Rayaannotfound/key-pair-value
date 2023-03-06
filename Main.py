# an object of WSGI application
from flask import Flask

from flashrouters import flash
from users import user
from questions import question

app = Flask(__name__)  # Flask constructor
app.register_blueprint(flash)
app.register_blueprint(user)
app.register_blueprint(question)


# A decorator used to tell the application
# which URL is associated function
#@app.route('/')
#def hello():
#    return 'Hi everyone its markiplier here'


# routing the decorator function hello_name


if __name__ == '__main__':


    app.run(debug=True)