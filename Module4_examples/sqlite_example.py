""" Creating and inserting data with SQLite"""
import sqlite3


def create_table(conn):
    curs = conn.cursor()
    create_statement = """
      CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(20),
        favorite_number INTEGER,
        least_favorite_number INTEGER
      );
    """
    curs.execute(create_statement)
    curs.close()
    conn.commit()


def insert_data(conn):
    curs = conn.cursor()
    my_data = [
        ('Antony', 7, 13),
        ('Nick', 77, 2),
        ('James', 6, 3),
    ]
    for data in my_data:
        pass

    curs.insert()
    curs.close()
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("example_db.sqlite3")
    create_table(conn)
    insert_data(conn)
