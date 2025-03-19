import sqlite3 as sqlite

USERNAME = ""


def Add_Username(username):
    global USERNAME
    try:
        with sqlite.connect("users.db") as conn:

            cursor = conn.cursor()

            USERNAME = username
            print(f"Add_Username= {USERNAME}")

            new_row: tuple[str, int] = (username, 0)
            cursor.execute("""INSERT INTO users (name, guesses)
                                VALUES (?, ?);""", new_row)

    except sqlite.OperationalError as e:
        print(e)


def Update_Guesses(final_num_guesses):
    global USERNAME
    try:
        with sqlite.connect("users.db") as conn:

            cursor = conn.cursor()

            print(f"Update_Guesses= {final_num_guesses, USERNAME}")

            updated_row: tuple[int, str] = (final_num_guesses, USERNAME)
            cursor.execute("""UPDATE users
                              SET guesses = ?
                              WHERE name LIKE ?;""", updated_row)

            USERNAME = ""

    except sqlite.OperationalError as e:
        print(e)

