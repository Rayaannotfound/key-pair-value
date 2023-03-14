from flask import Blueprint, render_template, request, make_response, redirect
import sqlite3
from flashcard import Flashcard

home = Blueprint('homepage', __name__, )



@home.route('/home', methods=['GET', 'POST'])
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
def createflash():
    duplicate = None
    if request.method == "POST":
        duplicate = False
        connect = sqlite3.connect('flashcard.db')
        cursor = connect.cursor()
        question = request.form.get("Question")
        answer = request.form.get("Answer")
        flashcard = Flashcard(question, answer)
        print(question)
        print(answer)
        cursor.execute("""SELECT question FROM flashcard""")
        results = cursor.fetchall()

        if results:
            for item in results:
                if item[0] == flashcard.question:
                    duplicate = True




        if duplicate ==False:
            cursor.execute("INSERT INTO flashcard VALUES (?,?)", (flashcard.question, flashcard.answer))
        else:
            print("Seems you already have that value..Try again")
        connect.commit()
        connect.close()

        # SQL code:
    return render_template("create.html", duplicate=duplicate)


@home.route('/delete/<query>')
def deleteFlash(query):
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

