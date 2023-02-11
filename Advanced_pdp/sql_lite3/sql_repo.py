import sqlite3

class ContactRepo:
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        

    def add(self, first_name, last_name, phone_number):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO contacts (first_name, last_name, phone_number)
            VALUES (?, ?, ?)
            """,
            (first_name, last_name, phone_number)
        )
        self.db.commit()
    

    def list(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT *
            FROM contacts
            """
        )
        return cursor.fetchall()

    def search(self, search_term):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT *
            FROM contacts
            WHERE first_name LIKE ? OR last_name LIKE ? OR phone_number LIKE ?
            """,
            (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%")
        )
        return cursor.fetchall()
