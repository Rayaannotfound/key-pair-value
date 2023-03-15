import sqlite3
connect = sqlite3.connect('../flashcard.db')
cursor = connect.cursor()

#cursor.execute("""create table flashcard
#(
#     question text primary key,
#     answer text,
#)""")

cursor.execute("""create table accounts
(
        id integer primary key autoincrement,
        username text,
        password text
)""")



# cursor.fetchall() gets every row
connect.commit()

connect.close()