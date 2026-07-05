import sqlite3

from database.schema import SCHEMA

from config.settings import DB_PATH


def initialize():

    conn = sqlite3.connect(DB_PATH)

    conn.executescript(SCHEMA)

    conn.commit()

    conn.close()


if __name__ == "__main__":

    initialize()

    print("Database Ready")