from .db import (
    get_connection,
    INSERT_STATEMENT,
    UPDATE_STATEMENT,
    SELECT_STATEMENT,
    RecordNotFoundException
)


class Book:
    connection = get_connection()

    def __init__(self, _id=None):
        self._id = None
        self._author = None
        self._title = None
        self._changed = False

        if _id:
            self.load(_id)

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @title.setter
    def title(self, value):
        self._title = value
        self._changed = True

    @author.setter
    def author(self, value):
        self._author = value
        self._changed = True

    def save(self):
        
        if not self._changed:
            return

        if not self.id:
            with self.connection as db:
                db.execute(INSERT_STATEMENT, (self.title, self.author))
                self._id = db.lastrowid
        else:
            with self.connection as db:
                db.execute(UPDATE_STATEMENT, (self.title, self.author, self.id))

    def load(self, _id):
        with self.connection as db:
            db.execute(SELECT_STATEMENT, (_id,))
            book = db.fetchone()

            if not book:
                raise RecordNotFoundException(f'Record with id({_id}) does not exists.')

            self._id = book[0]
            self.author = book[1]
            self._title = book[2]
