from flask import Blueprint, render_template, request, make_response
from database.database import Database
from flashcard import Flashcard

flash = Blueprint('flashrouters', __name__, )


@flash.route('/edit_question/', methods=['POST', 'GET'])
def update_question_flash():
    results = Database.get_instance().run_query("""SELECT question FROM flashcard""")
    print("These are the questions:")
    print(results)
    duplicate = None
    if request.method == "POST":
        question = request.form.get("Question")
        new_question = request.form.get("NewQuestion")

        if (new_question,) in results:
            duplicate = True
            print("That's a duplicate value")
        else:
            Database.get_instance().run_query("UPDATE flashcard SET question = (?) WHERE question = (?)", (new_question, question))
            duplicate = False
    return render_template("updatequestion.html", results=results, duplicate=duplicate)


@flash.route('/create', methods=['POST', 'GET'])
def create_flash():
    duplicate = None
    if request.method == "POST":
        duplicate = False
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
                    duplicate = True
        if not duplicate:
            db.run_query("INSERT INTO flashcard VALUES (?,?)", (flashcard.question, flashcard.answer))
        else:
            print("Seems you already have that value..Try again")

    return render_template("create.html", duplicate=duplicate)


@flash.route('/delete/<query>')
def delete_flash(query):
    print(f'attempting to delete: "{query}" from db...')
    results = Database.get_instance().run_query("SELECT answer, question FROM flashcard WHERE question=(?)", (query,))
    if results:
        answer = results[0][0]
        print(f'found row: question = "{query}", answer = "{answer}"')
        Database.get_instance().run_query("DELETE FROM flashcard WHERE question=(?) AND answer=(?)", (query, answer))
        print(f'Delete operation successful.')
    return redirect('/flashcards')


@flash.route('/update/', methods=['POST', 'GET'])
def update_flash():
    results = Database.get_instance().run_query("""SELECT question FROM flashcard""")
    print("These are the questions:")
    print(results)
    if request.method == "POST":
        question = request.form.get("Question")
        answer = request.form.get("Answer")
        flashcard = Flashcard(question, answer)
        print("Results after form results: ")
        print(results)
        print("Question: " + flashcard.question)
        print("Answer: " + flashcard.answer)
        Database.get_instance().run_query("UPDATE flashcard SET answer = (?) WHERE question = (?)", (flashcard.answer, flashcard.question))
    # [('Whats 9 + 10?q=', '21'), ('How can you perform decompression?', "I don't know")]
    # [('How can you perform decompression?',), ('Whats 9 + 10?q=',)]

    # Does the above cover situation of arriving at page by 'GET'?
    return render_template("update.html", results=results)


@flash.route('/flashcards')
def view_flash():
    results = Database.get_instance().run_query("""SELECT * FROM flashcard""")
    print(results)
    return render_template("flashcards.html", results=results)
