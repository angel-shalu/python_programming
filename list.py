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
ls = [ 7,22,14,5,9]
print(ls)              # it will print the complete list
print(type(ls))        # it will print the type of list
print(len(ls))         # it will print the lenght of list
print(ls[0])           # it will print the first element of list
ls[0] = "hello"        # it will change the first element of list
print(ls)

for i in ls:           # it will print all the element of list one by one
    print(i)


# ======================================= 
# LIST COMPREHENSION
ls = [ 7,22,14,5,9]    
ls.append(100)          # it will add 100 at the last of the list
print(ls)

ls = [ 7,22,14,5,9]
ls.append([100,700])     # it will add [100,700] as a single element at the last of the list
print(ls)            

# =====================================================
#======================================================
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
    choice = int(input("Enter your Choice:"))                # taking choice from user
    if(choice==1):                                           # add data
        ndata=int(input("Enter the data to be added:"))      # taking number of data to be added
        for i in range(ndata):                               # loop for number of data
            print(f"Enter the {i+1} data:")                  # taking data from user
            data = input("Enter the data:")                  # taking data from user
            ls.append(data)                                  # adding data to list
    elif(choice==2):                                         # read data
        print(ls)
    elif(choice==3):                                         # update data
        break

#================================================================   

# ================================================================
# LIST CONSTRUCTOR
ls = list((10,20,30,40,50))
print(ls)

ls1 = [13,25,37,49,51,73,88,23,54,11]
ls1 .sort()                 # asscending order me sort hoga 
print(ls1)
ls1 .reverse()              # reverse kregs 
print(ls1)

ls2 = [13,25,37,49,51]
x = max(ls2)                # particular list me se max value dega
print(x)

ls2 = [13,25,37,49,51]
x = min(ls2)               # particular list me se min value dega
print(x)

ls2 = [13,25,37,49,51]     # last me add krega 
ls2.extend([100,200,300])
print(ls2)

ls2.pop()                 # last element ko remmove krega
print(ls2)

ls2.pop(0)                # particular index ko remove krega
print(ls2)

ls2.insert(2,777)         # particular index pr value add krega
print(ls2)

ls2.remove(25)            # particular value ko remove krega
print(ls2)

index = ls2.index(49)    # particular value ka index dega
print(index)

ls3 = ls2.copy()         # ek list ko dusri list me copy krega
ls2.clear()              #  puri list ko clear krega
print(ls2)
print(ls3)

c = ls3.count(51)        # particular value kitni baar hai ye count krega
print(c)

    
# =========================================================
#WAP to find the second largest number from the list 78, 23, 15,9, 91, 97 without using inbuilt method or function of a list
# =========================================================

ls = [78, 23, 15, 9, 91, 97]
for i in range(len(ls)):                  # outer loop
    for j in range(i+1, len(ls)):         # inner loop
        if ls[i] > ls[j]:                 # comparison
            temp = ls[i]                  # swapping
            ls[i] = ls[j]                 
            ls[j] = temp
print("Second largest number is:", ls[-2])         # accessing second last element


ls = [78, 23, 15, 9, 91, 97]
print("Original list is:", ls)                #it will print original list
for i in range(len(ls)):                      # outer loop
    for j in range(i+1, len(ls)):             # inner loop
        if ls[i] > ls[j]:                     # comparison
            ls[i], ls[j] = ls[j], ls[i]       # swapping
print("Second largest number is:", ls[-2])

# --------------------using inbuilt method or function of a list--------------------

ls = [78, 23, 15, 9, 91, 97]
print("Original list is:", ls)
ls.sort()                                    # sort method
print("Original list is:", ls)
print("Second largest number is:", ls[-2])



# ==========================================================
# LIST COMPREHENSION
# ==========================================================
ls =[ i for i in range (1,101)]         # it will print counting from 1 to 100
print(ls)

# 2nd method
ls = []
for i in range(1, 101):      # it will print counting from 1 to 100
    ls.append(i)             # adding element to list
print(ls)

# ==========================================================

ls = [ i**2 for i in range (1,101)]      # it will print square of counting from 1 to 100
print(ls)

ls =[ i for i in range (65,91)]          # it will print ascii value from 65 to 90
for i in ls:
    print(i)                             # yaha pe ye print karega ascii value from 65 to 90
    print(chr(i))                        # it will print character of ascii value from 65 to 90
    print(chr(i), end=" ")
    
ls =[ i for i in range (97, 123)]        # it will print ascii value from 65 to 90
for i in ls:
    print(chr(i))
    print(chr(i), end=" ") 
    
# ==================================================
# Aise number ko print kro jiska ascci value parlidrome ho
# ==================================================    
ls = [i for i in range(32, 127)]
print(ls)                                  # it will print ascii value from 32 to 126
print("Lenght of the list :", len(ls))     # it will print lenght of the list

for i in ls:
    x = str(i)
    print(x)                              # it will print ascii value from 32 to 126
    if x == x[::-1]:
        print(chr(i), ":", i)             # it will print character whose ascii value is palindrome

# 2nd method
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

for i in range(1, 1001):         # loop from 1 to 1000
    j = 1                        # initialize j to 1
    while j * j <= i:            # check if j*j is less than or equal to i
        if j * j == i:           # check if j*j is equal to i
            print(i)             # print i if it is a perfect square
        j += 1                   # increment j


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