# Database functions in this file
# currently hardcoded to sqllite db
# however later can be refactored to be flexible to DB connected to

import sqlite3


class Database:

    db_instance = None

    def __init__(self, connection):
        self.connection_detail = connection

    @staticmethod
    def get_instance ():
        return Database.db_instance

    def db_initialise(self):
        if Database.db_instance is None:
            Database.db_instance = self
            return True
        else:
            return False

    def get_connect(self):
        connect = sqlite3.connect(self.connection_detail)
        return connect

    def close(self, connect):
        connect.close()

    def run_query (self, query, parameters=None):
        connect = self.get_connect()
        cursor = connect.cursor()
        if parameters is None:
            cursor.execute(query)
        else:
            cursor.execute(query, parameters)

        results = cursor.fetchall()
        print("DEBUG: sql command run")
        connect.commit()
        self.close(connect)
        return results



