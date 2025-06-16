from sqlite3 import *


def get_members():
    try:
        with connect("g_sheets.db") as conn:
            cursor = conn.cursor()
            members: set[str] = set()

            db_output: list[tuple[str, int]] = cursor.execute("SELECT name FROM members;").fetchall()

            for row in db_output:
                for name in row:
                    members.add(name)

            return members

    except OperationalError:
        print("Cannot access database")


def save(person_to_add: str):
    try:
        with connect("g_sheets.db") as conn:
            cursor = conn.cursor()

            cursor.execute("""  
            INSERT INTO members (name)
            VALUES (?)
            """, [(person_to_add)])
            # the parameter is put inside a 2D list because __parameters iterates through every element.

    except OperationalError:
        print("Cannot access database")


def remove(person_to_remove):
    try:
        with connect("g_sheets.db") as conn:
            cursor = conn.cursor()

            pattern = f"%{person_to_remove}%"  # .execute() can't recognize the wildcard syntax: %
            cursor.execute("""
            DELETE FROM members 
            WHERE name LIKE ?
            """, [(pattern)])

    except OperationalError:
        print("Cannot access database")