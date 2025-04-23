""" 1
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
You can display a string literal with the print() function:

"""
print("Hello")
print('Hello')


""" 2
Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

Multiline Strings
You can assign a multiline string to a variable by using three quotes:
Or three single quotes:
"""
a = "Hello"
print(a)

""" 3
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
Get the character at position 1 (remember that the first character has the position 0):
"""
a = "Hello, World!"
# print(a[1])
print(a[7])

""" 4
Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
Loop through the letters in the word "banana":
"""
for x in "banana":
  print(x)

""" 5
String Length
To get the length of a string, use the len() function.
The len() function returns the length of a string:
"""
a = "Hello, World!"
print(len(a))


# 6...   Checking the string   And result will be in the bollean form
txt= "I am happy."
print("happy" in txt)

# Checkl if not
txt= "I am happy."
print("go" not in txt)

txt= "I am happy."
if "go" not in txt :
    print("Go is not present in this line")