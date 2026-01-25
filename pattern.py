# # RIGHT ANGLE TRAINGELE PATTERN
"""
* 
* *
* * *
* * * *
* * * * *"""
n = int(input("Enter the number of rows: "))
print(n)

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
# ------------------------------------------------------------

def my_function(x):
    print("This is  a right angle trainglepattern program")
    for i in range(x):
        for j in range(i+1):
            print("*", end=" ")
        print()
my_function(5)


# ======================================================================================
def my_function(x):
    print("This is  a right angle traingle pattern program")
    for i in range(1, x+1):
        for j in range(1, x+1-i):
            print(" ", end=" ")
        for k in range(1, i+1):
            print("*", end=" ")
        print()
my_function(5)
    
    
# ======================================================================================
# TRIANGLE PATTERN
def my_function(x):
    print("This is  a  triangle pattern program")
    for i in range(1, x+1):
        for j in range(1, x+1-i):
            print(" ", end=" ")
        for k in range(1, i+1):
            print("*", end="   ")
        print()
my_function(5)
    

# ======================================================================================
# INVERTED TRIANGLE PATTERN

def my_function(x):
    for i in range(1, x+1):
        for j in range(1, x+1-i):
            print(" ", end=" ")
        for k in range(1, i+1):
            print("*", end="   ")
        print()
my_function(5)

def my_function1(x):
    for i in range(1, x+1):
        for k in range(1, i):
            print(" ", end=" ")
        for j in range(1, x+2-i):
            print("*", end="   ")
        print()
my_function1(5)
    
    

# ======================================================================================
# SAWASTIK PATTERN

def swastik_pattern(x):
    for i in range(1, x+1):
        for j in range(1, x+1):

            if (i == 5 and j == 5):
                print("*", end=" ")

            elif ((i == 1 and j < 5) or
                  (j == 9 and i < 5) or
                  (i == 9 and j > 5) or
                  (j == 1 and i > 5)):
                print("*", end=" ")

            else:
                print(" ", end=" ")
        print()
swastik_pattern(9)


# ======================================================================================
"""WAP to generate
a
bc
def
ghij
klmno"""

def char_pattern(n):
    x=97
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(x), end=" ")
            x+= 1
        print() 
char_pattern(5)

# ==================================================================================
"""
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15"""

def num_pattern(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(x, end=" ")
            x += 1
        print()

num_pattern(5)



# ======================================================================================
"""
a
ab
abc
abcd
abcde"""

def char_pattern(n):
    for i in range(1, n+1):
        x=97
        for j in range(1, i+1):
            print(chr(x), end=" ")
            x+= 1
        print() 
char_pattern(5)

# =====================================================================================
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

def num_pattern(n):
    for i in range(1, n+1):
        x = 1
        for j in range(1, i+1):
            print(x, end=" ")
            x += 1
        print()

num_pattern(5)




# ======================================================================================
"""
a
bb
ccc
dddd
eeeee"""

def char_pattern(n):
    x=97
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(x), end=" ")
        x+= 1
        print() 
char_pattern(5)


# ======================================================================================
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5"""

def num_pattern(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(x, end=" ")
        x += 1
        print()

num_pattern(5)


#============================================================================
"""
* * * * * * * * * 
* * * *   * * * *
* * *       * * *
* *           * * 
*               *
"""
n = 5

for i in range(n):
    # left stars
    for j in range(n - i):
        print("*", end=" ")

    # middle spaces
    for j in range(2*i):
        print(" ", end=" ")

    # right stars
    for j in range(n - i - 1):
        print("*", end=" ")

    print()

            
#====================================================================================
"""
* * * * *
* * * *
* * *
* *
*"""
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    

# ================================================================================
# SQUARE PATTERN 
# ================================================================================
n= int(input("Enter the Number of rows: "))
def squarer_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
squarer_pattern(n)
        
        
# ===================================================================================
# 
# ===================================================================================