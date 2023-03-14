# an object of WSGI application
from flask import Flask

from flashrouters import flash
from questions import question
from homepage import home
from userjoin import user
app = Flask(__name__)  # Flask constructor
app.register_blueprint(flash) #flashcard functionality: create, delete, update
app.register_blueprint(question) #redundant code
app.register_blueprint(home)
app.register_blueprint(user)





if __name__ == '__main__':


    app.run(debug=True)