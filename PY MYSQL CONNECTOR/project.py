import crud_operation_using_py_mysql
obj = crud_operation_using_py_mysql.Database_Connection()

while True:
    print("""
    Press 1 for add data
    Press 2 for read the data 
    Press 3 for update the data 
    Press 4 for delete the data 
    Press 5 for exit
    """)

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        print("Insert")
        roll_number = input("Enter the roll_number: ")
        name = input("Enter the name: ")
        branch = input("Enter the branch: ")
        address = input("Enter the address: ")

        obj.RecordInsert(roll_number, name, branch, address)

    elif choice == 2:
        print("Read")

    elif choice == 3:
        print("Update")

    elif choice == 4:
        print("Delete")

    elif choice == 5:
        print("Program closed...")
        break

    else:
        print("Wrong choice..")
