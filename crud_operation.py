# CRUD OPERATION OF LIST
ls = []

while(True):         # infinite loop
    print("""
          Press 1 for add data in list
          Press 2 for read the data 
          Press 3 for update the data 
          Press 4 for delete the data 
          Press 5 for exit.
          """)

    choice = int(input("Enter your Choice:"))    # taking choice from user

    # ---------------- CREATE ----------------
    if(choice==1):                              
        ndata = int(input("Enter the data to be added:"))
        for i in range(ndata):
            print(f"Enter the {i+1} data:")
            data = input("Enter the data:")
            ls.append(data)

    # ---------------- READ ----------------
    elif(choice==2):                            
        print("Read the data:")
        for i in ls:
            print(f"My data = {i}")

    # ---------------- UPDATE ----------------
    elif(choice==3):                            
        print("Update the data:")
        data = input("Enter the data to be updated:")
        try:
            x = ls.index(data)
            udata = input("Enter the updated data:")
            ls[x] = udata
            print("Data updated successfully.")
        except:
            print("Data not found.")

    # ---------------- DELETE ----------------
    elif(choice==4):                            
        print("Delete the data:")
        data = input("Enter the data to be deleted:")
        try:
            x = ls.index(data)
            ls.pop(x)
            print("Data deleted successfully.")
        except:
            print("Data not found.")

    # ---------------- EXIT ----------------
    elif(choice==5):                            
        print("Thanks for the operation.")
        break

    else:
        print("Your choice is Invalid.")







# ======================================================================================
# WAP to make a crud operation on tuple 
# ======================================================================================

tp = ()
while(True):         # infinite loop
    print("""
          Press 1 for add data in list
          Press 2 for read the data 
          Press 3 for update the data 
          Press 4 for delete the data 
          Press 5 for exit.
          """)
    choice = int(input("Enter your Choice:"))                # taking choice from user
    
    if(choice==1):          
        ls=list(tp)
        print("Create the data:")
        ndata = int(input("Enter the number of data: "))
        for i in range(ndata):
            print(f"Enter the data : {i+1}")
            data=input("Enter the data :")
            ls.append(data)
            tp=tuple(ls)
                                
    elif(choice==2):       
        print("Read the data:")
        for i in tp:
            print(f"My data = {i}")   
            
    elif(choice==3):                                        
        print("Update the data:")
        ls=list(tp)
        data=input("Enter the data to be updated:")
        try:
            x=ls.index(data)
            udata=input("Enter the updated data:")
            ls[x]=udata
            tp=tuple(ls)
        except:
            print("Dta not found.")
            
    elif(choice==4):       
        print("Delete the data:")   
        ls=list(tp)
        data=input("Enter the data to be deleted:")
        try:
            x=ls.index(data)
            ls.pop(x)
            tp=tuple(ls)
        except:
            print("Data not found.")

    elif(choice==5):                                        
        print("Thanks for the operation:") 
        break
       
    else:
        print("You choice is Invalid.")
        continue
    
    


# ====================================================================================
# CRUD OPERATION USING SET
# ====================================================================================
s = set()
print(s)
while(True):         # infinite loop
    print("""
          Press 1 for add data in list
          Press 2 for read the data 
          Press 3 for update the data 
          Press 4 for delete the data 
          Press 5 for exit.
          """)
    choice = int(input("Enter your Choice:"))                # taking choice from user
    
    if(choice==1):          
        print("Create the data:")
        ndata = int(input("Enter the number of data: "))
        for i in range(ndata):
            print(f"Enter the data : {i+1}")
            data=input("Enter the data :")
            s.add(data)
                                
    elif(choice==2):       
        print("Read the data:")
        for i in s  :
            print(f"My data = {i}")
            
    elif(choice==3):                                        
        print("Update the data:")
        data=input("Enter the data to be updated:")
        try:
            s.remove(data)
            udata=input("Enter the updated data:")
            s.add(udata)
        except:
            print("Data not found.")
            
    elif(choice==4):       
        print("Delete the data:")   
        data=input("Enter the data to be deleted:")
        try:
            s.remove(data)
        except:
            print("Data not found.")

    elif(choice==5):                                        
        print("Thanks for the operation:") 
        break
       
    else:
        print("You choice is Invalid.")
        continue