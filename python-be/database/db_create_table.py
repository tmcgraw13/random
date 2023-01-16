from db_mydatabases import MyDatabase
from db_mydatabases import MyTables

from db_connections import execute_input

def main():
    dbName = MyDatabase.users
    execute_input(dbName, "DROP TABLE {tableName};".format(tableName=MyTables.user_tbl))
    sql_create_users_table = """ CREATE TABLE {tableName} (
                                        PersonId INT NOT NULL AUTO_INCREMENT,
                                        Username varchar(255) NOT NULL,
                                        PRIMARY KEY (PersonId),
                                        CONSTRAINT UC_Person UNIQUE (Username)
                                    ); """.format(tableName=MyTables.user_tbl)
    execute_input(dbName,sql_create_users_table)
    print(dbName + " Tables Successfully Created")


    dbName = MyDatabase.numbers
    execute_input(dbName, "DROP TABLE {tableName};".format(tableName=MyTables.random_tbl))
    sql_create_numbers_table = """ CREATE TABLE {tableName} (
                                        Id INT NOT NULL AUTO_INCREMENT,
                                        Random INT,
                                        PRIMARY KEY (Id)
                                    ); """.format(tableName=MyTables.random_tbl)
    execute_input(dbName,sql_create_numbers_table)
    print(dbName + " Tables Successfully Created")

    # print("COMPLETE")
    #sql_input=(val1,val2,val3,"INSERT INTO 'table' VALUES(%s,%s,%s)")



if __name__ == '__main__':
    main()