# # Q.1. Ask a number from user and print all the numbers from 1 to that number using while loop.
# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     print(i, end=' ')  # end=' ' ka matlab h ki print ke baad new line nahi aayegi, uske bad space aayega
#     i += 1  
    
    

# # Q.2. Ask a number from user and print the multiplication table of that number using while loop.
# num = int(input("Enter a number to print its multiplication table: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1
    
    
    
# # Q.3. Ask a number from user and print the factorial of that number using while loop.
# num = int(input("Enter a number to find its factorial: "))
# factorial = 1
# i = 1
# while i <= num:
#     factorial *= i  # factorial = factorial * i
#     i += 1
# print(f"The factorial of {num} is {factorial}")



# # Q.4. Ask a number from user and print the Fibonacci series up to that number using while loop.
# num = int(input("Enter a number to print Fibonacci series up to that number: "))
# a, b = 0, 1
# while a <= num:
#     print(a, end=' ')
#     a, b = b, a + b  # a ko b se replace kar do aur b ko a+b se replace kar do



# # Q.5. Ask a number N from user and print all the numbers from N to 1.
# num = int(input("Enter a number: "))
# i = num
# while i >= 1:
#     print(i, end=' ')
#     i= i - 1                # i -= 1 ka matlab h i ko 1 se kam kar do
    
    
    
# # Q.6. Ask start number and end number from user and print all the numbers from start to end using while loop.
# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# i = start
# while i <= end:
#     print(i, end=' ')
#     i += 1
    
    
    
# # Q.7. Calculate the sum of all the numbers from 1 to 10.
# i = 1
# total_sum = 0
# while i <= 10:
#     total_sum += i     # total_sum = total_sum + i
#     i += 1
# print(total_sum)
        
        
        
# # Q.8. Calculate the product of all the numbers from 1 to 10.
# i = 1
# total_product = 1
# while i <= 10:
#     total_product *= i     # total_product = total_product * i
#     i += 1
# print(total_product)




# Q.9. Calculate how many numbers divisible by 7 from 1 to 100.
    
i = 1
count = 0
while i <= 100:
    if i % 7 == 0:
        print(i, end=' ')     # ye code se kon kon num divide ho rha h wo ayega
        count += 1           # ye code se kitne num divide ho rha h wo count hoga
    i=i+1
print(f"\nTotal numbers divisible by 7 from 1 to 100: {count}")




# Q. 10. Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
i = 1
count = 0
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count += 1                   # ye code se kitne num divide ho rha h wo count hoga
    i=i+1
print(f"\nTotal numbers divisible by both 6 and 7 from 1 to 200: {count}")



# Q.11. WAP to calculate the sum of all the numbers divisible by 4 from 20 to 50.
i = 20
total_sum = 0
while i <= 50:
    if i % 4 == 0:
        total_sum += i     # total_sum = total_sum + i
    i=i+1
print(f"\nTotal sum of numbers divisible by 4 from 20 to 50: {total_sum}")




# Q.12. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.

i = 1
count = 0
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count += 1                   # ye code se kitne num divide ho rha h wo count hoga
    i=i+1           
    
    
    
# 13. Ask a number from the user and print the multiplication table of that number in reverse order using while loop.
num = int(input("Enter a number to print its multiplication table in reverse order: "))
i = 10
while i >= 1:
    print(f"{num} x {i} = {num * i}")
    i -= 1




# 13. Ask a number from the user and print the multiplication table of that number.
num = int(input("Enter a number to print its multiplication table "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


