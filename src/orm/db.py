import sqlite3
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(PROJECT_ROOT, 'books.sqlite')

INSERT_STATEMENT = 'INSERT INTO book (title, author) VALUES (?, ?)'
UPDATE_STATEMENT = 'UPDATE book SET title = ?, author = ? WHERE id = ?'
SELECT_STATEMENT = 'SELECT * FROM book WHERE id = ?'


class RecordNotFoundException(Exception):
    pass


class Connection:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)

    def __enter__(self):
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()


connection = None


def get_connection():
    global connection

    if not connection:
        connection = Connection()
    return connection


def create_database():
    statement = (
        'CREATE TABLE IF NOT EXISTS book ('
        '    id INTEGER PRIMARY KEY AUTOINCREMENT,'
        '    author VARCHAR(100) NOT NULL,'
        '    title VARCHAR(100) NOT NULL'
        ');'
    )
    connection = get_connection()
    with connection as db:
        db.execute(statement)


create_database()
