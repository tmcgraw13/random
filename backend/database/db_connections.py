import mysql.connector

def execute_input(mydb,sql_input):
    """ create a database connection to a MySQL database """
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password!",
        database=mydb
    )
    with conn:
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        print(sql_input)
        cur = conn.cursor()
        try:
            cur.execute(sql_input) #WHY DO YOU ADD A STAR see readme
            conn.commit() #required to make the changes
            print(mydb + "Successfully Executed Input")
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))


    