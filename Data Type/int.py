a = 10 
print(a)  # Output: 10
print(type(a))  # Output: <class 'int'>
print(a(type(a)))  # Output: 10 <class 'int'>

a = 100
b = 200
c = a + b
print(c)  # Output: 300
print(a,type(a))  # Output: 100<class 'int'>
print(b,type(b))  # Output: 200 <class 'int'>
print(c,type(c))  # Output: 300 <class 'int'>
print(id(a))  # Output: Unique identifier for variable a
print(a,b,c)  # Output: 100 200 300
print(type(a),type(b),type(c))  # Output: <class 'int'> <class 'int'> <class 'int'>


# ========================================================
# INT DATA TYPE WE CAN ALSO STORE DIFFERENT TYPE OF NUMMBER SYSTEM

"""NOTE :-  To Convert decimal number system value to binary number system value 
we use a pre defined function called bin()

Digits: 0 1
Total Digits=2
Base: 2 """

a = 0b1010  # Binary representation of 10
print(a)  # Output: 10
print(type(a))  # Output: <class 'int'> 
print(a,type(a))  # Output: 10 <class 'int'>

bin(11)  # Output: '0b1011'
bin(20)  # Output: '0b10100'

# -------------------------------------------------------
"""NOTE :-  To Convert decimal, binary, hexadecimal number system value into octal number system value 
we use a pre defined function called oct()

Digits: 0 1 2 3 4 5 6 7
Total Digits=8
Base: 8 """

a = 0o12  # Octal representation of 10
print(a)  # Output: 10  
print(type(a))  # Output: <class 'int'>

oct(11)  # Output: '0o13'
oct(20)  # Output: '0o24'
oct(8)   # Output: '0o10'

# -------------------------------------------------------
""" NOTE :-  To Convert decimal, binary, octal number system value into hexadecimal number system value 
we use a pre defined function called hex()

Digits: 0 1 2 3 4 5 6 7 8  9 
A(10) , B(11),  C(12),  D(13),  E(14),   F(15)
Base: 16"""

a = 0xA  # Hexadecimal representation of 10
print(a)  # Output: 10  
print(type(a))  # Output: <class 'int'>
print(a,type(a))  # Output: 10 <class 'int'>
hex(11)  # Output: '0xb'
hex(20)  # Output: '0x14'
hex(15)  # Output: '0xf'

a = 27
hex(a)  # Output: '0x1b'
oct(a)  # Output: '0o33'    
bin(a)  # Output: '0b11011'
print(a,type(a))  # Output: 27 <class 'int'>

a = 22
b = 7
c = a+b
print(c)  # Output: 29
print(a,type(a))  # Output: 22 <class 'int'>    
bin(c)  # Output: '0b11101'
oct(c)  # Output: '0o35'
hex(c)  # Output: '0x1d'









