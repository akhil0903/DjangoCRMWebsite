import mysql.connector

dataBase =mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password'
)

#prepare a curosr object

cursorObject = dataBase.cursor()

#create a databse

cursorObject.execute("CREATE DATABASE CRMWebsite")
print("CREATED!")