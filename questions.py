from flask import Blueprint, render_template, request


question = Blueprint('questions', __name__,)


@question.route('/cards')
def flashcards():
    return render_template("grid.html")


@question.route('/grid', methods=['POST', 'GET'])
def grid():
    if request.method == 'POST':
        results = request.form
        return render_template("flashcards.html", results=results)
