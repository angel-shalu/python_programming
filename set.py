# """ SET :- 
# When we want to represent a group of individual entity into an single entity, 

# A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
# *Note: Set items are unchangeable, but you can remove items and add new items.

# # Creating a Set
# myset = {"apple", "banana", "cherry"}
# print(myset)                    # Output: {'banana', 'cherry', 'apple'}
# print(type(myset))              # Output: <class 'set'>
# print(len(myset))               # Output: 3

# # =================================================
# # Methods in Set
# # =================================================
# # Method	                         Description
# # add()	                             Adds an element to the set
# # clear()	                         Removes all the elements from the set
# # copy()	                         Returns a copy of the set
# # difference()                       Returns a set containing the difference between two or more sets
# # difference_update()	             Removes the items in this set that are also included in another set
# # discard()	                         Removes the specified item
# # intersection()	                 Returns a set, that is the intersection of two other sets
# # intersection_update()	             Removes the items in this set that are not present in other,
# # issubset()	                     Returns True if all items in the set are present in another set
# # issuperset()	                     Returns True if all items in another set are present in this set
# # pop()	                             Removes an element from the set
# # remove()	                         Removes the specified element
# # symmetric_difference()	         Returns a set with the symmetric differences of two sets
# # symmetric_difference_update()	     inserts the symmetric differences from this set and another
# # union()	                         Return a set containing the union of sets
# # update()	                         Update the set with the union of this set and others
# # =================================================
# """


# s = {1,1,2,3,4,4,5}             # yaha pe dublicate value override ho jayegi 
# print(s)                        # Output: {1, 2, 3, 4, 5} (duplicates removed)
# print(type(s))                  # Output: <class 'set'>

# s = {1,1,1,1,1,3,3,3,3,2,2,2,2,5,6,67,7,8}
# print(s)                        # Output: {1, 2, 3, 5, 6, 67, 7, 8} (duplicates removed)

# s.add(7777)
# print(s)                        # Output: {1, 2, 3, 5, 6, 67, 7, 8, 7777}

# s.add("shalu")
# print(s)                        # Output: {1, 2, 3, 5, 6, 67, 7, 8, 7777, 'shalu'}


# s.discard(3)
# print(s)                        # Output: {1, 2, 67, 5, 6, 7, 8, 7777, 'shalu'}
# x = s.discard("shalu")          # agar item set me nahi hai to bhi error nahi dega
# print(s)                        # Output: {1, 2, 67, 5, 6, 7, 8, 7777}

# s.remove(2)                     # agar item set me nahi hai to error dega
# print(s)                        # Output: {1, 67, 5, 6, 7, 8, 7777}

# # x = s.remove(67)                # remove method koi value return nahi karta
# # print(x)                        # Output: None
# # x = s.remove(9999)              # KeyError: 9999 not found (q ki is me element nahi hai.......lekin discard me elemet ni hoga fir v error ni dega)
# # print(x)

# s.pop()                         # set me se random item remove karega
# print(s)

# s.update([8888,9999])
# print(s)                        # Output: {1, 5, 6, 7, 8, 7777, 8888, 9999}

# s1= s.copy()                        # set ka shallow copy banayega
# print(s1)

# s.clear()                       # set ke sare item remove kar dega
# print(s)                        # Output: set()



# # --------------------------union------------------------
# bjp={1,2,3,4,5}
# cong={3,4,5,6,7,8,9}
# x = bjp.union(cong)
# print(x)                            # Output: {1, 2, 3, 4,  5, 6, 7, 8, 9}
# print(bjp.union(cong))               # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# y = bjp | cong
# print(y)                            # Output: {1, 2, 3, 4,  5, 6, 7, 8, 9}  
# print(bjp | cong)                   # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}



# # --------------------------intersection------------------------
# z = bjp.intersection(cong)
# print(z)                            # Output: {3, 4, 5}
# print(bjp.intersection(cong))       # Output: {3, 4, 5}

# z1 = bjp & cong
# print(z1)                            # Output: {3, 4, 5}
# print(bjp & cong)                   # Output: {3, 4, 5}


# # --------------------------difference------------------------
# z2 =bjp.difference(cong)
# print(z2)                           # Output: {1, 2}    
# print(bjp.difference(cong))        # Output: {1, 2}


# # --------------------------frozenset------------------------
# bjp = frozenset(bjp)          # frozenset ek aisa set hota hai jisme hum elements ko change nahi kar sakte
# print(bjp)                    # Output: frozenset({1, 2, 3, 4, 5})
# print(type(bjp))              # Output: <class 'frozenset'>



# # ===================SET COMPREHENSION===================
# # Set comprehension is a concise way to create sets.
# # It consists of curly braces containing an expression followed by a for clause, and optionally, one or more if clauses to filter elements.
# # Syntax: {expression for item in iterable if condition}

# set1 = {i for i in range(10)}
# print(set1)                        # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# set1 = {i for i in range(1,100,5)}
# print(set1)                        # Output: {1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96}

# set1 = {i for i in range(100,0,-5)}
# print(set1)                        # Output: {100, 95, 90, 85  , 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5}



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