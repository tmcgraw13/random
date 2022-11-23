from db_mydatabases import MyDatabase
from db_connections import execute_input

def main():
    dbName = MyDatabase.numbers
    sql_create_numbers_table = """ CREATE TABLE random_tbl (
                                        id INT NOT NULL AUTO_INCREMENT,
                                        random INT,
                                        PRIMARY KEY (id)
                                    ); """
    
    # create a database connection
    execute_input(dbName,sql_create_numbers_table)



if __name__ == '__main__':
    main()