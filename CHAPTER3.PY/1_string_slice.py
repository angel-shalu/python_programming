"""STRING SLICING

A string in python can be sliced for getting a part of the strings.

Consider the following string:
Name= Harry => Lenght = 5 
     0 1 2 3 4.... slicing from front
     (-5) (-4) (-3) (-2) (-1)..... slicing from backward

The index in a sting starts from 0 to (length-1) in Python. 
In order to slice a string, we use the following syntax:

Name= Harry
sl = name [ind_start: ind_end]
first index included
last index is not included

sl [0:3] returns "har" → characters from 0 to 3
sl [1:3] returns "ar" → characters from 1 to 3

Negative Indices: Negative indices can also be used as shown in the figure above. -1 corresponds to the (length - 1) index, -2 to (length - 2)."""

# LENGTH
name = "Shalini"
print(len(name))

# BASIC INDEXING 
name = "Shalini"
slice = name[2:6] # Here 2 is included and 6 is excluded 
print(slice)

# If we want to print single character from the word then we use
character1 = name[4]
print(character1)