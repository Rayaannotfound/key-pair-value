from flask import Blueprint, render_template, request, make_response, redirect
import sqlite3
from flashcard import Flashcard

home = Blueprint('homepage', __name__, )


@home.route('/', methods=['GET', 'POST'])
def homepage():
    connect = sqlite3.connect('flashcard.db')
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM flashcard""")
    results = cursor.fetchall()
    print(results)
    connect.commit()
    connect.close()

    return render_template("homepage.html", results=results)


@home.route('/create', methods=['POST', 'GET'])
def create_flash():
    if request.method == "POST":
        connect = sqlite3.connect('flashcard.db')
        cursor = connect.cursor()
        question = request.form.get("Question")
        answer = request.form.get("Answer")
        flashcard = Flashcard(question, answer)
        print(question)
        print(answer)
        cursor.execute("INSERT INTO flashcard VALUES (?,?)", (flashcard.question, flashcard.answer))
        connect.commit()
        connect.close()

        # SQL code:

    return render_template("create.html")


@home.route('/delete/<query>')
def delete_flash(query):
    print(f'attempting to delete: "{query}" from db...')
    connect = sqlite3.connect('flashcard.db')
    cursor = connect.execute("SELECT answer question FROM flashcard WHERE question=(?)", (query,))
    answer = cursor.fetchone()[0]
    print(f'found row: question = "{query}", answer = "{answer}"')
    cursor.execute("DELETE FROM flashcard WHERE question=(?) AND answer=(?)", (query, answer))
    print(f'Delete operation successful.')
    connect.commit()
    connect.close()

    return redirect('/')


@home.route('/edit_question/', methods=['POST', 'GET'])
def update_question_flash():
    connect = sqlite3.connect('flashcard.db')
    cursor = connect.cursor()
    cursor.execute("""SELECT question FROM flashcard""")
    results = cursor.fetchall()
    print("These be the questions:")
    print(results)
    if request.method == "POST":
        question = request.form.get("Question")
        newquestion = request.form.get("NewQuestion")
        print("oh, the question is ", question)
        cursor.execute("UPDATE flashcard SET question = (?) WHERE question = (?)", (newquestion, question))
        connect.commit()
        connect.close()
    else:
        connect.commit()
        connect.close()
    return render_template("updatequestion.html", results=results)
    # [


@home.route('/update/', methods=['POST', 'GET'])
def update_flash():
    connect = sqlite3.connect('flashcard.db')
    cursor = connect.cursor()
    cursor.execute("""SELECT question FROM flashcard""")
    results = cursor.fetchall()
    print("These be the questions:")
    print(results)
    if request.method == "POST":
        question = request.form.get("Question")
        answer = request.form.get("Answer")
        flashcard = Flashcard(question, answer)
        print("Results after form results: ")
        print(results)
        print("Question: " + flashcard.question)
        print("Answer: " + flashcard.answer)
        cursor.execute("UPDATE flashcard SET answer = (?) WHERE question = (?)", (flashcard.answer, flashcard.question))
        connect.commit()
        connect.close()
    # [('Whats 9 + 10?q=', '21'), ('How can you perform decompression?', "I don't know")]
    # [('How can you perform decompression?',), ('Whats 9 + 10?q=',)]
    else:
        connect.commit()
        connect.close()
    # Does the above cover situation of arriving at page by 'GET'?

    return render_template("update.html", results=results)
