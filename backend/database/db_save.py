from database.db_connections import execute_input
from database.db_mydatabases import MyDatabase

def save_random_integer(number):
    database = MyDatabase.numbers
    sql = ''' INSERT INTO random_tbl (Random) VALUES({0}) '''
    sql_input = sql.format(number)
    print(sql_input)

    # create a database connection and execute input
    execute_input(database,sql_input)
    
def save_username(user):
    database = MyDatabase.users
    sql = ''' INSERT INTO user_tbl (Username) VALUES('{0}') '''
    sql_input = sql.format(user)
    print(sql_input)

    # create a database connection and execute input
    execute_input(database,sql_input)