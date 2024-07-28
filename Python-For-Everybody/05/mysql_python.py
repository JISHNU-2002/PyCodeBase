import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "jishnu2002",
        database = "PythonDB"
    )
    
    if(mydb.is_connected()):
        print("connected to mysql database")
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE PythonDB")
        
        cursor.execute("SHOW DATABASES")
        for db in cursor:
            print(db)
            
        cursor.execute("CREATE TABLE Pyfiles (filename VARCHAR(256), filesize INT)")
        
        cursor.execute("SHOW TABLES")
        for db in cursor:
            print(db)
            
        cursor.execute("SELECT * FROM Pyfiles")
        result = cursor.fetchall()
        for i in result:
            print(i)

except Error as e:
    print("error while connecting to database : ",e)
finally:
    if(mydb.is_connected()):
        cursor.close()
        mydb.close()
        print("disconnected from mysql database")
        
