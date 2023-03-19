import sqlite3

connect = sqlite3.connect('../flashcard.db')
cursor = connect.cursor()  # this file should only be ran once. Lines 7 to 11 create an accounts table for the
# username and password

# database DDL from actual database
cursor.execute("""create table accounts
(
    username text not null primary key,
    password text
)""")

# lines 14-19 creates a table for the flashcard properties
cursor.execute("""create table flashcard
(
    question text primary key,
    answer   text
)""")

# cursor.fetchall() gets every row
connect.commit()

connect.close()
