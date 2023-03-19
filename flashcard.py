class Flashcard:
    # creates an instance of the values that can be used for adding and getting values from the database
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return "Flashcard('{}', '{}', {})".format(self.question, self.answer)
