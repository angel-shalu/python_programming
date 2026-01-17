# """
# When we want to represent a group of individual entity into an single entity,
# then we can implement a tuple class to represent that group.

# NOTE : - Tuple is immutable (cannot be changed after creation) and ordered collection of elements.
# """

# tp = (1, 2, 3, 4, 5)
# print(tp)                        # Output: (1, 2, 3, 4, 5)
# print(type(tp))                  # Output: <class 'tuple'>
# print(tp[0])                     # Output: 1
# print(tp[-1])                    # Output: 5

# tp.append(6)                     # AttributeError: 'tuple' object has no attribute 'append'
# print(tp)

# tp.clear()                       # AttributeError: 'tuple' object has no attribute 'clear'
# print(tp)

# x = tp.count(3)                  # Counts occurrences of 3 in the tuple
# print(x)                         # Output: 1

# y = tp.index(4)                  # Finds the index of first occurrence of 4
# print(y)                         # Output: 3

# tp[0] = 10                       # TypeError: 'tuple' object does not support item assignment
# print(tp)



# ls = list(tp)                    # Convert tuple to list
# ls.append("hello")               # Now we can append to the list
# print(ls)                        # Output: [1, 2, 3, 4, 5, 'hello']
# tp = tuple(ls)                   # Convert list back to tuple
# print(tp)                        # Output: (1, 2, 3, 4, 5, 'hello')



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
