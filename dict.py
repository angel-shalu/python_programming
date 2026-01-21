# """ DICTIONARY :-
# Whenever we want to represent a grp of individual entity into a single entity, 
# in a key:value pair , key must be unique and immutable (string, number, tuple etc) but value can be of any type and can be duplicate.
# then we can implement a dictionary. 
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# NOTE:- Dictionary is mutable (we can change, add, remove items after creation)

# """

# # Creating a Dictionary
# mydict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(mydict)                    # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(type(mydict))              # Output: <class 'dict'>


# d =  {"name": "Shalu", "age": 20, "city": "Delhi", "name": "Shalini"}  # duplicate key 'name' override ho jayega
# print(d)                         # Output: {'name': 'Shalini', 'age': 20, 'city': 'Delhi'}

# d1 = {"name": "Shalu", "age": 20, "city": "Delhi"}
# print(d1)                        # Output: {'name': 'Shalu', 'age': 20, 'city': 'Delhi'}
# print(type(d1))                  # Output: <class 'dict'>
# print(len(d1))                   # Output: 3    
# print(d1["name"])                # Output: Shalu


# d1["age"] = 21                    # updating value
# print(d1)                         # Output: {'name': 'Shalu', 'age': 21, 'city': 'Delhi'}

# print(d1.keys())                  # Output: dict_keys(['name', 'age', 'city'])
# keys = d1.keys()
# print(keys)                       # Output: dict_keys(['name', 'age', 'city'])   

# print(d1.values())                # Output: dict_values(['Shalu', 21, 'Delhi'])
# print(d1.items())                 # Output: dict_items([('name', 'Shalu'), ('age', 21), ('city', 'Delhi')])

# d1.pop("age")                     # removing key:value pair
# print(d1)                         # Output: {'name': 'Shalu', 'city': 'Delhi'}

# d1.popitem()                      # removes last inserted key:value pair
# print(d1)                        # Output: {'name': 'Shalu'}

# d1["country"] = "India"          # adding new key:value pair
# print(d1)                        # Output: {'name': 'Shalu', 'country': 'India'}

# ====================================================================================
d={ "a":1, "b":2, "c":3}
d.setdefault("d",4)        # if key 'd' not present then add key:value pair otherwise do nothing
print(d)                   # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d.update({"a": 10, "e":5})   # update value of key 'a' and add new key:value pair 'e':5
print(d)                      # Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
d.update(a=22)                # another way to update value of key 'a'
print(d)                      # Output: {'a': 22, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# ---------------------------------------------------------------------------------------
for i in d.items():
    print(i)
    
for i, j in d.items():
    print(f"Key = {i} and Value = {j}")
    

# ====================================================================================
# CRUD OPERATION USING DICTIONARY
# ====================================================================================
dict = {}
print(dict)

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
            dict[data] = None  # Add the data to the dictionary
                                
    elif(choice==2):       
        print("Read the data:")
        for i in dict  :
            print(f"My data = {i}")
            
    elif(choice==3):                                        
        print("Update the data:")
        data=input("Enter the data to be updated:")
        try:
            dict.pop(data)
            udata=input("Enter the updated data:")
            dict[udata] = None  # Add the updated data
        except:
            print("Data not found.")
            
    elif(choice==4):       
        print("Delete the data:")   
        data=input("Enter the data to be deleted:")
        try:
            dict.pop(data)
        except:
            print("Data not found.")

    elif(choice==5):                                        
        print("Thanks for the operation:") 
        break
       
    else:
        print("You choice is Invalid.")
        continue