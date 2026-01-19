"""Agar kisi number ke digits ki power (jitne digits hain) ka sum usi number ke equal ho, 
to use Armstrong number kehte hain.

Example 1: 153 (Most famous example)

Digits: 1, 5, 3
Total digits = 3

Calculation:
1³ + 5³ + 3³
= 1 + 125 + 27
= 153

Result = 153
153 ek Armstrong number hai


Example 2: 9474 (4-digit Armstrong)
Digits: 9, 4, 7, 4
Total digits = 4
Calculation:
9⁴ + 4⁴ + 7⁴ + 4⁴   
= 6561 + 256 + 2401 + 256
= 9474
Result = 9474
9474 ek Armstrong number hai


======Non-Armstrong Example=========
Example: 123
1³ + 2³ + 3³
= 1 + 8 + 27
= 36 ≠ 123
Armstrong number nahi hai
"""

num = int(input("Enter the number:"))
original_num = num
print("Original Number:", original_num)

sum_of_powers = 0   
num_digits = len(str(num))     
while num > 0:
    digit = num % 10                          # % 10 se last digit nikalte hain
    sum_of_powers += digit ** num_digits      # us digit ki power (len k barabar) nikal k sum m add kar diya
    num = num // 10                           # last digit ko hatane k liye //10 kar diya
    
# #Palindrome check
# rev = 0
# temp = original_num 
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp = temp // 10

rev = int(str(original_num)[::-1])  # ye ek line m palindrome check karne ka shortcut hai
    
if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")  
      
elif rev == original_num:
    print(f"{original_num} is also a palindrome.")   
    
else:
    print(f"{original_num} is a Normal number.")


