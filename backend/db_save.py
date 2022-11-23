from db_connections import execute_input
from db_mydatabases import MyDatabase

def save_random_integer(number):
    database = MyDatabase.numbers
    sql = ''' INSERT INTO random_tbl (random) VALUES(%s) '''
    input = (sql, (number,))

    # create a database connection and execute input
    execute_input(database,input)
   
