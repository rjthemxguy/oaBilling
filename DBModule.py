
import mysql.connector

class database_class:
    def __init__(self, hostname, username, password, databaseName)

        mydb = mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=password,
            database=databaseName
            )

        mycursor = mydb.cursor()