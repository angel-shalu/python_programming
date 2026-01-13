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


# # ======================================= 
# # LIST COMPREHENSION
# ls = [ 7,22,14,5,9]
# ls.append(100)
# print(ls)

# ls = [ 7,22,14,5,9]
# ls.append([100,700])
# print(ls)    #it will give the list inside lidt that is sublist

# # =====================================================
# #======================================================
# # CRUD OPERATION OF LIST
# ls = []
# while(True):
#     print("""
#           Press 1 for add data in list
#           Press 2 for read the data 
#           Press 3 for update the data 
#           Press 4 for delete the data 
#           Press 5 for exit.
#           """)
#     choice = int(input("Enter your Choice:"))
#     if(choice==1):
#         ndata=int(input("Enter the data to be added:"))
#         for i in range(ndata):
#             print(f"Enter the {i+1} data:")
#             data = input("Enter the data:")
#             ls.append(data)
#     elif(choice==2):
#         print(ls)
#     elif(choice==3):
#         break

# #================================================================   
# ================================================================
# LIST CONSTRUCTOR
ls = list((10,20,30,40,50))
print(ls)

ls1 = [13,25,37,49,51,73,88,23,54,11]
ls1 .sort()    # asscending order me sort hoga 
print(ls1)
ls1 .reverse() # reverse kregs 
print(ls1)

ls2 = [13,25,37,49,51]
x = max(ls2)
print(x)

ls2 = [13,25,37,49,51]
x = min(ls2)   
print(x)

ls2 = [13,25,37,49,51]  # last me add krega 
ls2.extend([100,200,300])
print(ls2)

ls2.pop()  # last element ko remmove krega
print(ls2)
ls2.pop(0)   # particular index ko remove krega
print(ls2)

ls2.insert(2,777)  # particular index pr value add krega
print(ls2)
ls2.remove(25)   # particular value ko remove krega
print(ls2)
index = ls2.index(49)    # particular value ka index dega
print(index)

ls3 = ls2.copy()   # ek list ko dusri list me copy krega
ls2.clear()      #  puri list ko clear krega
print(ls2)
print(ls3)

c = ls3.count(51)   # particular value kitni baar hai ye count krega
print(c)

    
# =========================================================
#WAP to find the second largest number from the list 78, 23, 15,9, 91, 97 without using inbuilt method or function of a list
# =========================================================

ls = [78, 23, 15, 9, 91, 97]
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if ls[i] > ls[j]:
            temp = ls[i]
            ls[i] = ls[j]
            ls[j] = temp
print("Second largest number is:", ls[-2])


ls = [78, 23, 15, 9, 91, 97]
for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print("Second largest number is:", ls[-2])

# --------------------using inbuilt method or function of a list--------------------

ls = [78, 23, 15, 9, 91, 97]
ls.sort()
print("Original list is:", ls)
print("Second largest number is:", ls[-2])



# ==========================================================
# LIST COMPREHENSION
# ==========================================================
ls =[ i for i in range (1,101)]   # it will print counting from 1 to 100
print(ls)
ls = [ i**2 for i in range (1,101)] # it will print square of counting from 1 to 100
print(ls)

ls =[ i for i in range (65,91)]   # it will print ascii value from 65 to 90
for i in ls:
    print(chr(i))
    print(chr(i), end=" ")    # it will print character of ascii value from 65 to 90
    
ls =[ i for i in range (97, 123)]   # it will print ascii value from 65 to 90
for i in ls:
    print(chr(i))
    print(chr(i), end=" ") 
    
# ==================================================
# Aise number ko print kro jiska ascci value parlidrome ho
# ==================================================    
ls = [i for i in range(32, 127)]
for i in ls:    
    x = str(i)
    if x == x[::-1]:
        print(chr(i), ":", i)
        
# =========================================================
# WAP to find consonante and vovel from A to Z character in a list and seprate them and stored in another list 
letters = []
vowels = []
consonants = []

for ch in range(65, 91):   # A to Z
    letters.append(chr(ch))

for ch in letters:
    if ch in "AEIOU":
        vowels.append(ch)
    else:
        consonants.append(ch)

print("Vowels:", vowels)
print("Consonants:", consonants)

# =========================================================
# WAP to find all the perfect square of a number from 1 to 1000 numbers
print("Perfect square numbers from 1 to 1000:")

for i in range(1, 1001):
    j = 1
    while j * j <= i:
        if j * j == i:
            print(i)
        j += 1


# =========================================================
# WAP to make CRUD OPERATIONS using choice based in a list
# =========================================================
lst = []

while True:
    print("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = input("Enter value: ")
        lst.append(val)

    elif choice == 2:
        print("List:", lst)

    elif choice == 3:
        pos = int(input("Enter index to update: "))
        val = input("Enter new value: ")
        if pos < len(lst):
            lst[pos] = val
        else:
            print("Invalid index")

    elif choice == 4:
        pos = int(input("Enter index to delete: "))
        if pos < len(lst):
            lst.pop(pos)
        else:
            print("Invalid index")

    elif choice == 5:
        break

    else:
        print("Invalid choice")
# ==========================================================