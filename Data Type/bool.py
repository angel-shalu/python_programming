a = True
b = False
print(a)        # Output: True
print(b)        # Output: False  
print(type(a))  # Output: <class 'bool'>
print(type(b))  # Output: <class 'bool'>   
print(a,(type(a)))  # Output: True <class 'bool'>
print(b,(type(b)))  # Output: False <class 'bool'>

print(a + 1)    # Output: 2
print(b + 1)    # Output: 1

print(int(a))   # Output: 1
print(int(b))   # Output: 0 

print(float(a)) # Output: 1.0
print(float(b)) # Output: 0.0   

a=True
b=False
c=a+b
print(c)        # Output: 1
print(type(c))  # Output: <class 'int'>
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
print(not b)    # Output: True
print(a is b)   # Output: False
print(a is True)  # Output: True
print(b is False) # Output: True    
print(a == b)    # Output: False
print(a == True)  # Output: True
print(b == False) # Output: True    
print(a != b)    # Output: True
print(a != True)  # Output: False
print(b != False) # Output: False
print(bool(1))   # Output: True
print(bool(0))   # Output: False
print(bool(-1))  # Output: True
print(bool(""))  # Output: False
print(bool("Hello")) # Output: True
print(bool([]))      # Output: False    

print(True-False)   # Output: 1
print(True+2+False) # Output: 3
print(True+2*3)   # Output: 7
print(True-2+False)     # Output: -1
print(True*3+False)     # Output: 3 
print(0b1111+True)  # Output: 16
print(0xF-True)   # Output: 14
print(3.5+False)  # Output: 3.5
print(2.5*True)   # Output: 2.5
print(4/2+False)  # Output: 2.0
print(5//2*True)  # Output: 2
print(5%2+False)  # Output: 1
