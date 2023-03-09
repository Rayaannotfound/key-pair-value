class Flashcard:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


    def __repr__(self):
        return "Flashcard('{}', '{}', {})".format(self.question, self.answer)