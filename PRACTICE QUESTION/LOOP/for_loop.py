# Q.1. Ask a number from user and print all the numbers from 1 to that number using while loop.
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i, end=' ')   
    

# Q.2. Ask a number from user and print the multiplication table of that number using while loop.
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
    
    
# Q.3. Ask a number from user and print the factorial of that number using while loop.
num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i  # factorial = factorial * i 
print(f"The factorial of {num} is {factorial}")



# Q.4. Ask a number from user and print the Fibonacci series up to that number using while loop.
num = int(input("Enter a number to print Fibonacci series up to that number: "))
a, b = 0, 1
for i in range(num + 1):    
    if a > num:
        break
    print(a, end=' ')
    a, b = b, a + b      # a ko b se replace kar do aur b ko a+b se replace kar do  



# Q.5. Ask a number N from user and print all the numbers from N to 1.
num = int(input("Enter a number: "))
for i in range(num, 0, -1):
    print(i, end=' ')   
    
    
    
# Q.6. Ask start number and end number from user and print all the numbers from start to end using while loop.
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
for i in range(start, end + 1):
    print(i, end=' ')
    
    
    
# Q.7. Calculate the sum of all the numbers from 1 to 10.
total_sum = 0
for i in range(1, 11):
    total_sum += i     # total_sum = total_sum + i
print(total_sum)

        
        
# Q.8. Calculate the product of all the numbers from 1 to 10.
total_product = 1
for i in range(1, 11):
    total_product *= i     # total_product = total_product * i
print(total_product)




# Q.9. Calculate how many numbers divisible by 7 from 1 to 100.
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1                   # ye code se kitne num divide ho rha h wo count hoga   



# Q. 10. Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
count = 0
for i in range(1, 201):
    if i % 6 == 0 and i % 7 == 0:
        count += 1                   # ye code se kitne num divide ho rha h wo count hoga

        


# Q.11. WAP to calculate the sum of all the numbers divisible by 4 from 20 to 50.
total_sum = 0
for i in range(20, 51):
    if i % 4 == 0:
        total_sum += i     # total_sum = total_sum + i
print(f"The sum of all numbers divisible by 4 from 20 to 50 is: {total_sum}")



# Q.12. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.
count = 0
for i in range(1, 201):
    if i % 6 == 0 and i % 7 == 0:
        count += 1                   # ye code se kitne num divide ho rha h wo count hoga          
    
    
    
# 13. Ask a number from the user and print the multiplication table of that number in reverse order using while loop.
num = int(input("Enter a number to print its multiplication table in reverse order: "))
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num * i}")   
    


# 13. Ask a number from the user and print the multiplication table of that number.
num = int(input("Enter a number to print its multiplication table "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")   

