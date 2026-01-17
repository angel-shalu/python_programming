"""
An anagram is a word or phrase made by rearranging the letters of another word or phrase, using all the same letters exactly once.

Example:
listen → silent ✅ (same letters, just rearranged)
evil → live ✅
dusty → study ✅

Not an anagram:
cat → cut ❌ (letters are changed, not just rearranged)

In one line:
Anagram = same letters, different order. 😊
    """


# ---------------------------------------------------------
# WAP to check  TWO string is anagram or not without using inbuilt function
# ---------------------------------------------------------
str1 = "adbc"
str2 = "abcd"
c = 0
if(len(str1) != len(str2)):
    print("The strings are not anagrams.")
else:
    for i in range(len(str1)):
        for j in range(len(str2)):
            if (i == j):
                c+=1
                break
    if c == len(str1):
        print("The strings are anagrams.")  
    else:
        print("The strings are not anagrams.")
        

str1 = "aaaa"
str2 = "abcd"
c = 0
if(len(str1) != len(str2)):
    print("The strings are not anagrams.")
else:
    for i in range(len(str1)):
        for j in range(len(str2)):
            if (i == j):
                c+=1
                break
    if c == len(str1):
        print("The strings are anagrams.")  
    else:
        print("The strings are not anagrams.")
        


# -------------- INPUT TAKING FROM THE USER------------

# str1 = input("Enter first string: ")    
# str2 = input("Enter second string: ")
# if(len(str1) != len(str2)):
#     print("The strings are not anagrams.")
# else:
#     for i in range(str1):
#         for j in range(str2):
#             if (i == j):
#                 c+=1
#                 break
#     if c == len(str1):
#         print("The strings are anagrams.")  
#     else:
#         print("The strings are not anagrams.")