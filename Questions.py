# ============================================================
# WAP TO FIND THE SUM OF PRIME NUMBERS BETWEEN TWO USER INPUT
# ===========================================================
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

prime_sum = 0
while num1 <= num2:
    i = 1
    count = 0

    while i <= num1:
        if num1 % i == 0:
            count += 1
        i += 1

    if count == 2:
        prime_sum = prime_sum + num1

    num1 += 1   # move to next number
print("Sum of Prime Numbers =", prime_sum)


# ==========================================
# WAP to print mathematics table
# ==========================================
num = int(input("Enter the number: "))
i = 1

while i <= 10:
    math_table = num * i
    print(num, "*", i, "=", math_table)
    i += 1
    
    
# ===================================================
# WAP to find the LCM and input taken from the user
# ===================================================
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

max_num = max(num1, num2)

while True:
    if max_num % num1 == 0 and max_num % num2 == 0:
        print("LCM =", max_num)
        break
    max_num += 1


# ==========================================
""" WAP to print 
    A
    B C
    D E F
    G H I J
    K L M N O"""
#==========================================
num = 65
i = 1

while i <= 5:
    j = 1
    while j <= i:
        print(chr(num), end=" ")
        num += 1
        j += 1
    print()
    i += 1
    
    
    
    
    
# ==========================================================
"""     S  T R I N G
          P R O G R A M M I N G """  
          
# ==========================================================
# ==========================================================
# WAP to find the character whose ascii value is prime from string taken from the user
# ===========================================================
s = input("Enter the string: ")

for i in s:
    x = ord(i)
    count = 0
    i = 1

    while i <= x:
        if x % i == 0:
            count += 1
        i += 1

    if count == 2:
        print(chr(x))
        print(x)


# # ==========================================================
# WAP to arrange a string in the asscending order input taken from the user
# ===========================================================
s = input("Enter the string: ")
s = list(s)
for i in range (len(s)):
    for j in range(i+1, len(s)):
        x = ord(s[i])
        y = ord(s[j])   
        if s[i] > s[j]:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
print(s)

# ----------------------------------------------------------
# 2nd method to arrange a string in ascending order
# ----------------------------------------------------------
s = input("Enter the string: ")
n=len(s)
for i in range(len(s)):
    for j in range(i + 1, n):
        if ord(s[i]) > ord(s[j]):
            temp = s[i]
            # swap by rebuilding string
            s = s[:i] + s[j] + s[i+1:j] + temp + s[j+1:]

print(s)

# ========================================================
# WAP to multiple two input using russian multipliication
# ========================================================

s = int(input("Enter first number: "))
t = int(input("Enter second number: "))
result = 0
while s >= 1:
    if s % 2 != 0:
        result = result + t
    s = s // 2
    t = t * 2
print("Multiplication is:", result)


 
# =================================================================    
"""    L I S T 
    P R O G R A M M I N G  """
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

# ---------using inbuilt method or function of a list---------

ls = [78, 23, 15, 9, 91, 97]
print("Original list is:", ls)
ls.sort()                                    # sort method
print("Original list is:", ls)
print("Second largest number is:", ls[-2])



# ==================================================
# Aise number ko print kro jiska ascci value parlidrome ho
# ==================================================    
ls = [i for i in range(65, 91)]            # it will create a list of ascii value from 65 to 90
print(ls)                                  # it will print ascii value from 32 to 126
print("Lenght of the list :", len(ls))     # it will print lenght of the list

for i in ls:
    x = str(i)
    print(x)                              # it will print ascii value from 32 to 126
    if x == x[::-1]:
        print(chr(i), ":", i)             # it will print character whose ascii value is palindrome

# ------------------------------------------------
# 2nd method
ls = [i for i in range(65, 91)]
ls1 = []
for j in ls:                                # it will create a list of ascii value from 65 to 90
    rev = 0                                 # initialize rev to 0
    temp = j                                # store the value of j in temp
    while (j != 0):                         # loop until j is not equal to 0
        digit = temp % 10                   # get the last digit of temp
        rev = rev * 10 + digit              # build the reverse number
        j = j // 10                         # remove the last digit of temp
    if temp == rev:                         # check if temp is equal to rev
        print(chr(temp), ":", temp)         # print the character whose ascii value is palindrome
        ls1.append(temp)                    # append the palindrome ascii value to the list
print("List of palindrome ascii values:", ls1)
        

       
    
# =========================================================
# WAP to find consonante and vovel from A to Z character in a list and seprate them and stored in another list 
# =========================================================
letters = []
vowels = []
consonants = []

for i in range(65, 91):   # A to Z
    letters.append(chr(i))

for i in letters:
    if i in "AEIOU":
        vowels.append(i)
    else:
        consonants.append(i)

print("Vowels:", vowels)
print("Consonants:", consonants)

# 2nd method
letters = []
vowels = []
consonants = []

for i in range(65, 91):   # A to Z
    if(chr(i) == "A" or chr(i) == "E" or chr(i) == "I" or chr(i) == "O" or chr(i) == "U"):
        vowels.append(chr(i))
    else:
        consonants.append(chr(i))

print("Vowels:", vowels)
print("Consonants:", consonants)


# =========================================================
# WAP to find all the perfect square of a number from 1 to 1000 numbers
# =========================================================
print("Perfect square numbers from 1 to 1000:")

for i in range(1, 1001):         # loop from 1 to 1000
    j = 1                        # initialize j to 1
    while j * j <= i:            # check if j*j is less than or equal to i
        if j * j == i:           # check if j*j is equal to i
            print(i)             # print i if it is a perfect square
        j += 1                   # increment j
        


# ==========================================================    
# WAP to arrange a string in the asscending order input taken from the user
# ===========================================================
s = input("Enter the string: ")
n=len(s)
for i in range(len(s)):
    for j in range(i + 1, n):
        if ord(s[i]) > ord(s[j]):
            temp = s[i]
            # swap by rebuilding string
            s = s[:i] + s[j] + s[i+1:j] + temp + s[j+1:]
print(s)



# ==========================================================
# WAP to check  TWO string is anagram or not
# ==========================================================
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")   
# if(len(str1) != len(str2)):
#     print("The strings are not anagrams.")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
    
    
    
# ---------------------------------------------------------
# WAP to check  TWO string is anagram or not without using inbuilt function
# ---------------------------------------------------------
str1 = "aaaa"
str2 = "abcd"
c = 0
if(len(str1) != len(str2)):
    print("The strings are not anagrams.")
else:
    for i in range(len(str1)):
        for j in range(len(str2)):
            if (i == j):
                c+=1
                break
    if c == len(str1):
        print("The strings are anagrams.")  
    else:
        print("The strings are not anagrams.")

# -------------- INPUT TAKING FROM THE USER------------

str1 = input("Enter first string: ")    
str2 = input("Enter second string: ")
if(len(str1) != len(str2)):
    print("The strings are not anagrams.")
else:
    for i in range(str1):
        for j in range(str2):
            if (i == j):
                c+=1
                break
    if c == len(str1):
        print("The strings are anagrams.")  
    else:
        print("The strings are not anagrams.")
    
        
        
# =========================================================
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
        
            
# ==========================================================
# WAP to find the aramstrong number and palindrome number
# ==========================================================
num = int(input("Enter the number:"))
original_num = num
print("Original Number:", original_num)

sum_of_powers = 0   
num_digits = len(str(num))     
while num > 0:
    digit = num % 10                          # % 10 se last digit nikalte hain
    sum_of_powers += digit ** num_digits      # us digit ki power (len k barabar) nikal k sum m add kar diya
    num = num // 10                           # last digit ko hatane k liye //10 kar diya
    
# #Palindrome check
# rev = 0
# temp = original_num 
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp = temp // 10

rev = int(str(original_num)[::-1])  # ye ek line m palindrome check karne ka shortcut hai
    
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")  
      
elif rev == original_num:
    print(f"{original_num} is also a palindrome.")   
    
else:
    print(f"{original_num} is a Normal number.")


# ==========================================================`
# WAP hailstone series
n = int(input("Enter a number: "))
print(n, end=" ")
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print("→", n, end=" ")
# ==========================================================
# WAP to generate the hailstone sequence (Collatz sequence) for a given number n
# ==========================================================
ls = []
def hailstone_sequence(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
        ls.append(n)
hailstone_sequence(10)
print(ls)