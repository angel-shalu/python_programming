num = int(input("Enter number: "))
rev = int(str(num)[::-1])

if num == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome")



#===============================================================
# ==================================================
# Aise number ko print kro jiska ascci value parlidrome ho
# ==================================================    
ls = [i for i in range(65, 91)]            # it will create a list of ascii value from 65 to 90
print(ls)                                  # it will print ascii value from 32 to 126
print("Lenght of the list :", len(ls))     # it will print lenght of the list

for i in ls:
    x = str(i)
    print(x)                              # it will print ascii value from 32 to 126
    if x == x[::-1]:
        print(chr(i), ":", i)             # it will print character whose ascii value is palindrome

# ------------------------------------------------
# 2nd method
ls = [i for i in range(65, 91)]
ls1 = []
for j in ls:                                # it will create a list of ascii value from 65 to 90
    rev = 0                                 # initialize rev to 0
    temp = j                                # store the value of j in temp
    while (j != 0):                         # loop until j is not equal to 0
        digit = temp % 10                   # get the last digit of temp
        rev = rev * 10 + digit              # build the reverse number
        j = j // 10                         # remove the last digit of temp
    if temp == rev:                         # check if temp is equal to rev
        print(chr(temp), ":", temp)         # print the character whose ascii value is palindrome
        ls1.append(temp)                    # append the palindrome ascii value to the list
print("List of palindrome ascii values:", ls1)
        