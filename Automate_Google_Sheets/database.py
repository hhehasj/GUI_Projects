from sqlite3 import *


def get_members():
    try:
        with connect("g_sheets.db") as conn:
            members: set[str] = set()
            cursor = conn.cursor()

            db_output: list[tuple[str, str]] = cursor.execute("SELECT name FROM members;").fetchall()

            for row in db_output:
                for name in row:
                    members.add(name)

            return members

    except OperationalError:
        print("Cannot access database")


if __name__ == '__main__':
    get_members()