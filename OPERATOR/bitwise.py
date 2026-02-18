"""BIWISE OPERATOR

    """
# ------------------------------------------------------
# BITWISE AND OPERATOR
# 

   
a = 10     #00001010
b = 11     #00001011
c = a & b  #00001010
print(c)

# -------------------------------------------------------
# BITWISE OR OPERATIOR
# If both bits are 0 then result should be 0 otherwise 1

a = 10   #00001010
b = 11   #00001011
c = a|b  #00001011
print(c)

# -----------------------------------------------------------
# BIWISE XOR OPERATOR
# If both the bits will be same then result will be 0 otherwise 1


a = 10   #00001010
b = 11   #00001011
c = a^b  #00000001
print(c)


# ----------------------------------------------------------
# BITWISE NOT OPERATOR
# It is a unary operator and it is also known as complement operator    
# -----------------------------------------------------------
a = 10   #00001010
b = ~a   #11110101
print(b)

c = ~b   #00001010
print(c)



# -----------------------------------------------------------
# BITWISE LEFT SHIFT OPERATOR
# It shifts the bits of the number to the left by specified number of positions and fills the vacated bits with 0
# -----------------------------------------------------------
a = 10      #00001010
b = a << 1  #00010100    
print(b)

c = a << 2  #00101000
print(c)

x = c << 3  #01010000
print(x)


# -----------------------------------------------------------
# BITWISE RIGHT SHIFT OPERATOR
# It shifts the bits of the number to the right by specified number of positions and fills the vacated bits with 0
# -----------------------------------------------------------
a = 10      #00001010
b = a >> 1  #00000101   
print(b)

c = a >> 2  #00000010
print(c)

x = a >> 3  #00000001
print(x)

