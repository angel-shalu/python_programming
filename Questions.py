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
ls = [i for i in range(32, 127)]
print(ls)                                  # it will print ascii value from 32 to 126
print("Lenght of the list :", len(ls))     # it will print lenght of the list

for i in ls:
    x = str(i)
    print(x)                              # it will print ascii value from 32 to 126
    if x == x[::-1]:
        print(chr(i), ":", i)             # it will print character whose ascii value is palindrome

# ------------------------------------------------
# 2nd method
ls = [i for i in range(32, 127)]
for i in ls:    
    x = str(i)
    if x == x[::-1]:
        print(chr(i), ":", i)
        
        
        

# =========================================================
# WAP to find consonante and vovel from A to Z character in a list and seprate them and stored in another list 
# =========================================================
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
