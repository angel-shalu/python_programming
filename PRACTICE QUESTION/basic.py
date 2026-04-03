"""Q.1. Write a python program to add two numbers entered by the user."""

num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
sum = num1 + num2
print(f"The sum is: {sum}")



#Q.2. Convert a string to an interger and vice versa.
# String to Integer
str_num = "123"
print(str_num, type(str_num))
number = int(str_num, type(str_num))
print(f"String to Integer: {number}, Type: {type(number)}")

# Integer to String
int_num = 456
str_num = str(int_num)
print(f"Integer to String: {str_num}, Type: {type(str_num)}")



# Q.3. Write a python program to find the area of a rectangle using user input for length and width.
length = int(input("Enter the length of the rectangle = "))
width = int(input("Enter the width of the rectangle = "))
area = length * width
print(f"The area of the rectangle is: {area}")




# Q.4. Write a python progeram to calculate the average of three numbers enterd by the user.
num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))
num3 = int(input("Enter the third number = "))
average = (num1 + num2 + num3) / 3
print(f"The average of the three numbers is: {average}")



""" Q.5. WAP that converts temperature in Fahrenheit to Celsius and vice versa.
    a. Fahrenheit to Celsius: C = (F - 32) * 5/9
    b. Celsius to Fahrenheit: F = (C * 9/5) + 32
"""
# Fahrenheit to Celsius
f = float(input("Enter temperature in Fahrenheit = "))
c = (f - 32) * 5/9
print(f"Temperature in Celsius: {f} Fahrenheit = {c} Celsius")

# Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius = "))
f = (c * 9/5) + 32
print(f"Temperature in Fahrenheit: {c} Celsius = {f} Fahrenheit")



# Q.6. Write a python program to find the largest of three numbers entered by the user.
num1 = int(input("Enter the first number = "))      
num2 = int(input("Enter the second number = "))
num3 = int(input("Enter the third number = "))
largest = max(num1, num2, num3)
print(f"The largest of the three numbers is: {largest}")

       
       
#Q.7. Calculate sum of 5 subjects marks and find the percentage.
maths = int(input("Enter marks for Maths = "))
science = int(input("Enter marks for Science = "))  
english = int(input("Enter marks for English = "))
history = int(input("Enter marks for History = "))
geography = int(input("Enter marks for Geography = "))
total_marks = maths + science + english + history + geography
percentage = (total_marks / 500) * 100
print(f"Total Marks: {total_marks}, Percentage: {percentage}%")

# 2nd method using list:
marks = []
for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1} = "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
print(f"Total Marks: {total_marks}, Percentage: {percentage}%")



# Q.8. Convert a flot to integer and vice versa.
# Float to Integer
float_num = 3.14
int_num = int(float_num)
print(f"Float to Integer: {float_num} -> {int_num}")

# Integer to Float
int_num = 42
float_num = float(int_num)
print(f"Integer to Float: {int_num} -> {float_num}")    



"""Q.9. Ask number of game played in a tournament.
     Ask the user of games won and number of games loss.
     Calculate number of tie and total points'
     (1 win = 4 points, 1 tie = 2 points, 1 loss = 0 points)""" 
     
games_played = int(input("Enter the number of games played in the tournament = "))
games_won = int(input("Enter the number of games won = "))
games_lost = int(input("Enter the number of games lost = "))

games_ties = games_played - games_won - games_lost
print(f"Number of ties: {games_ties}")

total_points = (games_won * 4) + (games_ties * 2) + (games_lost * 0)
print(f"Total points: {total_points}")



# Q.10. Write a python program to find the square of a number entered by the user.
num = int(input("Enter a number to find its square = "))
square = num ** 2
print(f"The square of {num} is: {square}")


# Q.11. Write a python program to find the cube of a number entered by the user.
num = int(input("Enter a number to find its cube = "))  
cube = num ** 3
print(f"The cube of {num} is: {cube}")


# Q.12. Write a python program to find the factorial of a number entered by the user.
num = int(input("Enter a number to find its factorial = "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")

                
