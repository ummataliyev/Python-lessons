import sys

import sqlite3

from sql_repo import ContactRepo


try:
    with sqlite3.connect("contact.db") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                first_name VARCHAR,
                last_name VARCHAR,
                phone_number VARCHAR
            )
            """
        )

except Exception as e:
    print("An error occurred:", e)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("only 1 argument is required")

    available_commands = ('add', 'list', 'search')
    command = sys.argv[1]
    print(command)

    if command not in available_commands:
        sys.exit(f"Unknown command: {command}, available commands")
    

    with sqlite3.connect("contact.db") as db:
        repo = ContactRepo(db)
        if command == "add":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone_number = input("Phone number: ")
            repo.add(first_name, last_name, phone_number)
            print("Contact Successfully Created")
        
        if command == "list":
            contacts = repo.list()
            print(contacts, sep= "\n")

        if command == "search":
            first_name = input("First name: ")
            contacts = repo.search(first_name)
            print(contacts, sep= "\n")
            