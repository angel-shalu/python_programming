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
        

    # CREATE
    def RecordInsert(self, roll_number, name, branch, address):
        self.roll_number = roll_number
        self.name = name
        self.branch = branch
        self.address = address
        
        query = "Insert into student_details (roll_number, name, branch, address) values(%s,%s,%s,%s)"
        values = [self.roll_number, self.name, self.branch, self.address]
        self.mycursor.execute(query, values)
        self.mydb_connection.commit()
        print("Record inserted successfully...")
    
    
    # READ
    def ReadRecord(self):
        query = "SELECT * FROM student_details"
        self.mycursor.execute(query)
        records = self.mycursor.fetchall()
        print("\nRoll | Name | Branch | Address")
        for row in records:
            print(row)
  
  
    # UPDATE
    def UpdateRecord(self):
        roll_number = input("Enter roll number to update: ")
        branch = input("Enter the new branch: ")
        address = input("Enter the new address: ")
        query = """
            UPDATE student_details
            SET branch = %s, address = %s
            WHERE roll_number = %s
            """
        values = (branch, address, roll_number)
        self.mycursor.execute(query, values)
        self.mydb_connection.commit()
        print("Record updated successfully")
        
        
    # SEARCH
    def SearchRecord(self):
        roll_number = input("Enter roll number to search: ")
        query = """
            SELECT * FROM student_details
            WHERE roll_number = %s
            """
        values = [roll_number]
        self.mycursor.execute(query, values)
        records = self.mycursor.fetchall()
        count = self.mycursor.rowcount
        if count>=1:
            print(records)
        else:
            print("No data found...")
        print("Record search successfully")
      
        
    # DELETE   
    def DeleteRecord(self):
        roll_number = input("Enter roll number to delete: ")
        query = "DELETE FROM student_details WHERE roll_number = %s"
        values = [roll_number]
        self.mycursor.execute(query, values)
        self.mydb_connection.commit()
        print("Record deleted successfully")
        

