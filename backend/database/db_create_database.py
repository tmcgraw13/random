import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE numbersdb")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
  print(db[0])
print("Database Successfully Created")