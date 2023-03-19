from flask import Blueprint, render_template, request, make_response, redirect
from database.database import Database
from flashcard import Flashcard
from flask_login import login_required

flash = Blueprint('flashrouters', __name__, )


@flash.route('/edit_question/', methods=['POST', 'GET'])
@login_required
def update_question_flash():
    # gets the questions to push to the dropdown box
    results = Database.get_instance().run_query("""SELECT question FROM flashcard""")
    print("These are the questions:")
    print(results)
    duplicate = None
    # handles the post requests from the form
    if request.method == "POST":
        question = request.form.get("Question")
        new_question = request.form.get("NewQuestion")

        # does not allow data to be pushed if it is a duplicate
        if (new_question,) in results:
            duplicate = True
            print("That's a duplicate value")
        else:
            Database.get_instance().run_query("UPDATE flashcard SET question = (?) WHERE question = (?)",
                                              (new_question, question))  # updates the database with the new data
            duplicate = False
    return render_template("updatequestion.html", results=results, duplicate=duplicate)  # renders the html file to be
    # used


@flash.route('/create', methods=['POST', 'GET'])
@login_required
def create_flash():
    duplicate = None
    if request.method == "POST":
        duplicate = False
        # gets the data from the form and gets the existing results
        db = Database.get_instance()
        question = request.form.get("Question")
        answer = request.form.get("Answer")
        flashcard = Flashcard(question, answer)
        print(question)
        print(answer)
        results = db.run_query("""SELECT question FROM flashcard""")

        if results:
            for item in results:
                if item[0] == flashcard.question:
                    duplicate = True  # checks for duplicates- if true data won't be created
        if not duplicate:
            db.run_query("INSERT INTO flashcard VALUES (?,?)",
                         (flashcard.question, flashcard.answer))  # inserts data into the database
        else:
            print("Seems you already have that value..Try again")

    return render_template("create.html", duplicate=duplicate)  # renders the html file to be used


@flash.route('/delete/<query>')
@login_required
def delete_flash(query):
    # handles deleting the data
    print(f'attempting to delete: "{query}" from db...')
    results = Database.get_instance().run_query("SELECT answer, question FROM flashcard WHERE question=(?)", (query,))
    # gets the correct value to delete and deletes it
    if results:
        answer = results[0][0]
        print(f'found row: question = "{query}", answer = "{answer}"')
        Database.get_instance().run_query("DELETE FROM flashcard WHERE question=(?) AND answer=(?)", (query, answer))
        print(f'Delete operation successful.')
    return redirect('/flashcards')


@flash.route('/update/', methods=['POST', 'GET'])
@login_required
def update_flash():
    # gets the existing questions to display in thr dropdown
    results = Database.get_instance().run_query("""SELECT question FROM flashcard""")
    print("These are the questions:")
    print(results)
    if request.method == "POST":
        # gets the data from the database and adds it to the database,
        question = request.form.get("Question")
        answer = request.form.get("Answer")
        flashcard = Flashcard(question, answer)
        print("Results after form results: ")
        print(results)
        print("Question: " + flashcard.question)
        print("Answer: " + flashcard.answer)
        Database.get_instance().run_query("UPDATE flashcard SET answer = (?) WHERE question = (?)",
                                          (flashcard.answer, flashcard.question))
    return render_template("update.html", results=results)  # renders the html file to be used


@flash.route('/flashcards')
@login_required
def view_flash():
    # gets data from the database to display to the page
    results = Database.get_instance().run_query("""SELECT * FROM flashcard""")
    print(results)
    return render_template("flashcards.html", results=results)  # renders the html file to be used
