import mysql.connector
from db_mydatabases import MyHost


mydb = mysql.connector.connect(
  host=MyHost.cloud,
  user="root",
  password="Password!"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE numbersdb")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
  print(db[0])
print("Database Successfully Created")