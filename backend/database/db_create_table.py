from db_mydatabases import MyDatabase
from db_connections import execute_input

def main():
    dbName = MyDatabase.numbers
    sql_create_numbers_table = """ CREATE TABLE %s (
                                        id INT NOT NULL AUTO_INCREMENT,
                                        random INT,
                                        PRIMARY KEY (id)
                                    ); """.format()
    
    # create a database connection
    execute_input(dbName,sql_create_numbers_table)


    #sql_input=(val1,val2,val3,"INSERT INTO 'table' VALUES(%s,%s,%s)")



if __name__ == '__main__':
    main()