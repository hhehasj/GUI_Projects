import sqlite3


def add_username(connection, username: tuple[str, int]):
    sqlite_statement = '''INSERT INTO users (name, guesses)
                          VALUES (?, ?)'''

    cursor = connection.cursor()

    cursor.execute(sqlite_statement, username)


def Connect(username: str):

    try:
        with sqlite3.connect("users.db") as conn:

            # creates a row and puts it into the database.
            new_row = (username, 0)
            add_username(conn, new_row)

    except sqlite3.OperationalError as e:
        print(e)
