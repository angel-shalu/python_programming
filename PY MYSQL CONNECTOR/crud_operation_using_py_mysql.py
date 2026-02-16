# Make a simple project using python & mysql, Make a simple ceud operation, CREATE, READ, UPDATE & DELETE using choice based.


import mysql.connector

class Database_Connection:
    def __init__(self):
        self.mydb_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "2005",
            database = "student"
        )
        
        self.mycursor = self.mydb_connection.cursor()
        print("Database connected successfully...")
        
    def RecordInsert(self, roll_number, name, branch, address):
        self.roll_number = roll_number
        self.name = name
        self.branch = branch
        self.address = address
        
        sql = "Insert into student_details (name, roll_number, class, address) values(%s,%s,%s,%s)"
        value = [self.roll_number, self.name, self.branch, self.address]
        self.mycursor.execute(sql, value)
        self.mydb.commit()
        print("Record inserted successfully...")
        
        
        
        
        

        
Obj = Database_Connection()
        
