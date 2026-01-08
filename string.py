# # String with for loop
# for i in range(10):
#     print(i)
    
# for i in range(1,10):   # strat, stop
#     print(i)
    
# for i in range(1,10,2):  # start, stop, step
#     print(i)


# # =============================    
# str = "shalini"   
# print(type(str))

# l = len(str)
# print(l)

# s = "welcome"
# for i in s:
#     print(s)
    
# s = "welcome"
# for i in s:
#     print(i)


# =================================   
# WAP TO REVERSE THE STRING WELCOME
# =================================
str = "welcome"
for i in range(len(str)):
    print(str[i])

# ====================================
s = "welcome"
rev = ""

for i in range(len(s)):
    rev = s[i] + rev

print("Original String:", s)
print("Reversed String:", rev)

# ====================================
s = "welcome"
rev = ""

for i in range(len(s)):
    rev = s[i] + rev      # use character, not index
    print(rev * 2)

# ====================================

# STRING METHOD
### capitalize(): Converts the first character the string to Capital Letter

str = "welcome"  
x = str.capitalize()
print(x)

str = "welcome"   # it will convert all the letter in the upper case 
x = str.upper()
print(x)

str = "welcome"   # it will count the letter e
x = str.count("e")
print(x)

str = "welcome"  # slicing 
x = str[0:4:2]
print(x)

str = "welcome"  # slicing
x = str[::-1]
print(x)


### find(): Returns the index of first occurrence of substring
str = "welcome"  # slicing
x = str.find("e")  # agr letter h to index number dega 
print(x)

str = "welcome"  # slicing
x = str.find(x)   # agr letter ni h to -1 return krega
print(x)

str = "welcome"  # slicing
x = str.index("e",2,7) # ye last index ko ni lega us re phle wala ko lega 
print(x)

### endswith(): Checks if a string ends with a specified ending
str = "welcome"
x = str.endswith("e")
# x = str.startswith("e")
print(x)

# ==========================================================
# WAP to find the character whose ascii value is prime from string taken from the user
# ===========================================================