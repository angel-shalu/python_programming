a = 3.4
print(a) # Output: 3.4
print(type(a)) # Output: <class 'float'>
print(a, type(a)) # Output: 3.4 <class 'float'> 

a=2.3
b=4.5
c=a+b
print(c) # Output: 6.8
print(type(c)) # Output: <class 'float'>
print(c, type(c)) # Output: 6.8 <class 'float'>

a=2.3
b=4.5
c=a*b
print(c) # Output: 10.35        
print(type(c)) # Output: <class 'float'>
print(c, type(c)) # Output: 10.35 <class 'float'>

# ===============================================
# =>we can also use float data type store Scientific Notation Values
# (Mantisa e  Exponent) and whose eqv floating point value is   Mantisa x 10 to the power Exponent

"""Yaha pe  3 *10 to the power 2 = 3 * 100 = 300.0"""
a=3e2
print(a,type(a)) # Output: 300.0 <class 'float'>
b=4.5e3
print(b,type(b)) # Output: 4500.0 <class 'float'>   
c=a+b
print(c,type(c)) # Output: 4800.0 <class 'float'>

"""Yah pe  4 *10 to the power -2 = 4/100 = 0.04"""
b=4e-2
print(b,type(b)) # Output: 0.04 <class 'float'>