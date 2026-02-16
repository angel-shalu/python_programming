import mysql.connector
print("Connection Success")

mydb_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2005",
    database = "student"
     
)

mycursor = mydb_connection.cursor()
sql ="select*from student_details"
mycursor.execute(sql)
my_data = mycursor.fetchall()
for i in my_data:
    print(i)
