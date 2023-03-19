# an object of WSGI application
from flask import Flask, session
from flashrouters import flash
from homepage import home
from userjoin import user_join
from database.database import Database

app = Flask(__name__)  # Flask constructor
app.config['SECRET_KEY'] = 'sorrylol2'


@app.before_request
def before_request():
    session.permanent = False
    session.modified = True


def main():
    global app
    app.register_blueprint(flash)  # flashcard functionality: create, delete, update
    app.register_blueprint(home)
    app.register_blueprint(user_join)
    database = Database('flashcard.db')
    database.db_initialise()
    app.run(debug=True)


if __name__ == '__main__':
    main()