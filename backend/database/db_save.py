from database.db_connections import execute_input
from database.db_mydatabases import MyDatabase

def save_random_integer(number):
    database = MyDatabase.numbers
    sql = ''' INSERT INTO random_tbl (random) VALUES(%s) '''
    sql_input = sql.format(number)

    # create a database connection and execute input
    execute_input(database,sql_input)
    
   
