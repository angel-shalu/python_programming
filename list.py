# SEQUENCIAL DATA TYPE
""" 
LIST :-
When ever we want torepresent a group of indivisual intity into an single intity , where insertion order is to be preserved
and dat should be homogeneous as well as hetrogeneous then we can implement a list
NOTE:- LIST IS A MUTABLE AND ORDERED DATA TYPE(Changes can be allowed)
       Syntax of list :- ls[,,,,,,,,,,]
       eg:- ls = [10,20.5,"hello",True]
       print(ls)
       print(type(ls))
       list are iterable
       
"""
# ls = [ 7,22,14,5,9]
# print(ls)
# print(type(ls))   
# print(len(ls))
# print(ls[0])
# ls[0] = "hello"
# print(ls)

# for i in ls:
#     print(i)


# ======================================= 
# LIST COMPREHENSION
ls = [ 7,22,14,5,9]
ls.append(100)
print(ls)

ls = [ 7,22,14,5,9]
ls.append([100,700])
print(ls)    #it will give the list inside lidt that is sublist

# =====================================================


# CRUD OPERATION OF LIST
ls = []
while(True):
    print("""
          Press 1 for add data in list
          Press 2 for read the data 
          Press 3 for update the data 
          Press 4 for delete the data 
          Press 5 for exit.
          """)
    choice = int(input("Enter your Choice:"))
    if(choice==1):
        ndata=int(input("Enter the data to be added:"))
        for i in range(ndata):
            print(f"Enter the {i+1} data:")
            data = input("Enter the data:")
            ls.append(data)
    elif(choice==2):
        print(ls)
    elif(choice==3):
        break
    
# ================================================================
# WAP to 

    
    