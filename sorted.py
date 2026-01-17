"""  S O R T E D  LIST  """
# ==========================================================
# WAP to check  TWO string is anagram or not
# ==========================================================
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")   
# if(len(str1) != len(str2)):
#     print("The strings are not anagrams.")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")