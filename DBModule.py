
import mysql.connector

class database_class:
    def __init__(self, hostname, username, password, databaseName):



        self.mydb = mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=password,
            database=databaseName
            )

        self.mycursor = self.mydb.cursor(buffered=True)

    def getCPT(self, emgCode):

        self.code = emgCode

        sql = "SELECT CPT FROM codes WHERE code=" + "'" + emgCode + "'"

        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchone()

        return self.myresult

    def getPrice(self, CPT):



        sql = "SELECT price FROM comp WHERE hcpcs=" + "'" + CPT + "'"

        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchone()

        return self.myresult