"""Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:
Example
Convert from one type to another:"""

x = 1    # int
#convert from int to float:
a = float(x)
print(a)
print(type(a))

y = 2.8  # float
#convert from float to int:
b = int(y)
print(b)
print(type(b))

z = 1j   # complex
#convert from int to complex:
c = complex(x)
print(c)
print(type(c))


a=77
b=str(a)
print(b)
print(type(b))



"""Random Number :_ Python does not have a random() function to make a random number,
 but Python has a built-in module called random that can be used to make random numbers:
Example
Import the random module, and display a random number from 1 to 6:"""

import random
print(random.randrange(1, 7))