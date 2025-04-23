"""
OPERATORS IN PYTHON

Following are some common operators in python:

1. Arithmetic operators: +,-,*,/etc.
2. Assignment operators: =, +=, -= etc.
3. Comparison operators: ==, >, >=, <, != etc.
4. Logical operators: and, or, not.


7+8=15
here 7 and 8 are OPERANDS / + is OPERATOR And 15 is result

"""


# Arithmetic  operator

# Addition
a = 32
b = 67
c = a+b
print(c)

# Subtraction
x = 5
y = 3
print(x - y)

# Multiplication
x = 5
y = 3
print(x * y)

# Division
x = 15
y = 3
print(x / y)

# Modulus
x = 5
y = 3
print(x % y)

# Exponentiation
x = 5
y = 3
print(x ** y)

# Floor division
x = 5
y = 3
print(x // y)





#assignment operators
a = 7-2 #assign 7-2 in a
print(a)
b = 7
b +=3 #increment the value of b by 3 and then assign it to b 
# b -=3 #Decrement the value of b by 3 and then assign it to b 
# Here u can devide or multiple also
print(b)   


#comparison operators  :- its written value is always boolean
a = 5>9
print(a)

d = 5!=4
print(d)

x = 5
y = 3
print(x > y)  # returns True because 5 is greater than 3




#logical operators
e = True or False
print(e)
#Truth table of 'or'
print("True or False is",True or False)
print("True or True is",True or True)
print("False or True is",False or True)
print("False or False is",False or False)

#Truth table of 'and'
print("True and False is",True and False)
print("True and True is",True and True)
print("False and True is",False and True)
print("False and False is",False and False)

print(not(True))

x = 5
print(x > 3 and x < 10)   # returns True because 5 is greater than 3 AND 5 is less than 10

x = 5
print(x > 3 or x < 4)   # returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

x = 5
print(not(x > 3 and x < 10))  # returns False because not is used to reverse the result




