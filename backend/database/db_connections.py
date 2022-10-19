import mysql.connector
from env import MyCurrentEnv


def execute_input(mydb,input):
    """ create a database connection to a MySQL database """
    
    conn = mysql.connector.connect(
        host=MyCurrentEnv.host,
        user="root",
        password="Password!",
        database=mydb
    )
    with conn:
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        print(input)
        cur = conn.cursor()
        try:
            cur.execute(*input) #WHY DO YOU ADD A STAR see readme
            conn.commit() #required to make the changes
            print(mydb + "Successfully Executed Input")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))


    