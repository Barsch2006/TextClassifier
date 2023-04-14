from sqlite3 import Connection, Cursor, connect

class Database:
    def __init__(self) -> None:
        self.connection: Connection = connect('sqlite.db')
        self.cursor = self.connection.cursor()
    
    def all(self, sql: str, params: ...) -> list:
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Exception as err:
            print(err)
            return []

    def run(self, sql: str, params: ...) -> None:
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
        except Exception as err:
            print(err)
