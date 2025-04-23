# Problem 1 :- Write a python program to add two number
a=7
b=9
c=a+b
print(c)

a=int(input("Enter the first number :"))  # Taking input from the user
b=int(input("Enter the first number :"))
print("Sum = ",a+b)


# PROBLEM 2 :-   WAP to find the remainder when a number is dividible by z
a=36
b=7
print(" Remainder when a is divisible by b is :" , a % b)


# PROBLEM 3 :-   Check the type of variables assigne using input() function
a=input("Enter the number a :")
print(type(a))


# PROBLEM :- 4. Use comparison operator to find out whether a given variable a is greater than 'b' or not. Take a = 34 and b = 80
a = int(input("Enter the First Number :"))
b = int(input("Enter the Second Number :"))
print("a is greater than b :", a > b)


# 5. Write a python program to find an average of two numbers entered by the user.
a = int(input("Enter the First Number is: "))
b = int(input("Enter the Second Number is: "))
print("The average of these two numbers is:", (a + b) / 2)


# 6. Write a python program to calculate the square of a number entered by the user.
a=int(input("Enter your Number :"))
print("The square of the number is :", a * a) 
print("The square of the number is :", a ** 2) 
# print("The square of the number is :", a ^ 2)   It is incoorect in finding square in python