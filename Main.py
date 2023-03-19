# an object of WSGI application
from flask import Flask, session
from flashrouters import flash
from homepage import home
from userjoin import user_join, init_flask_login
from database.database import Database

app = Flask(__name__)  # Flask constructor
app.config['SECRET_KEY'] = 'sorrylol2'  # provides safety for encryption


@app.before_request
def before_request():
    session.permanent = False
    session.modified = True  # modifies the session allowing a user to stay logged in


def main():
    global app  # makes app global to be used elsewhere
    app.register_blueprint(flash)  # flashcard functionality: create, delete, update
    app.register_blueprint(home)
    app.register_blueprint(user_join)
    # blueprint is used throughout different files
    # but it adds those files to the flask application so flask knows which files to look for
    init_flask_login(app)
    database = Database('flashcard.db')
    database.db_initialise()  # initialises the database and a means of logging in
    app.run(debug=True)  # runs the app from here


if __name__ == '__main__':
    main()
