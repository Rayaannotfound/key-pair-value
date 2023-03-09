import sqlite3
from flashcard import flashcard
connect = sqlite3.connect('flashcard.db')
cursor = connect.cursor()

#cursor.execute("""create table flashcard
# (
#     question   text
#         primary key,
#     answer     text,
#     questionID integer
# )""")




# cursor.fetchall() gets every row
connect.commit()

connect.close()