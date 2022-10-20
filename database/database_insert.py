import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_number(conn, number):
    """
    Create a new random number into the numbers table
    :param conn:
    :param random:
    :return: number id
    """
    sql = ''' INSERT INTO numbers(random) VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (number,))
    conn.commit()
    return cur.lastrowid

def main():
    database = r"pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        create_number(conn, 35)

        


if __name__ == '__main__':
    main()