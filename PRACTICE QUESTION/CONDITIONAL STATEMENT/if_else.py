# Q.1. WAP thattakes an integer input and prints wheter it's positive or negative. (Consider 0 as positive)
num = int(input("Enter an integer: "))
if num >= 0:
    print(f"{num} is positive.")
else:
    print(f"{num} is negative.")
    
    
#Q.2. WAP that takes a character input and checks whether it's a vowel or consonant.
char = input("Enter a character: ")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" or char=="A" or char=="E" or char=="I" or char=="O" or char=="U":
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
    

# Q.3. WAP that takes two numbers as input and checks if the first number is divisible by the second number.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}.")
else:
    print(f"{num1} is not divisible by {num2}.")


"""Q.4. WAP a student will no allowed to sit in exam if his/her attendance is less than 75%. 
    Take the following input from user:
    Total number of classes held
    Number of classes attended
    
    1.print percentage of class attended
    2.print whether the student is allowed to sit in exam or not."""
    
classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: ")) 
attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance percentage: {attendance_percentage:.2f}%")     # :.2f ka matlab h do digit tak percentage dikhana
if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is not allowed to sit in the exam.")
    
    
# Q.5. WAP to check if number is divisible by 2 and 3 but not by 8
num = int(input("Enter an integer: "))
if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
    print(f"{num} is divisible by 2 and 3 but not by 8.")
else:
    print(f"{num} does not meet the criteria.")
    
    
# Q.6. WAP to check if a year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")    
else:
    print(f"{year} is not a leap year.")
    
    
    
# Q.7. WAP to print the last digit of a number (NOT IF ELSE QUESTION)
num = int(input("Enter an integer: "))
last_digit = num % 10
print(f"The last digit of {num} is: {last_digit}")



# Q.8. WAP to check if the last digit of a number is divisible by 5 or not.
num = int(input("Enter an integer: "))
last_digit = num % 10
if last_digit % 5 == 0:
    print(f"The last digit of {num} is divisible by 5.")
else:
    print(f"The last digit of {num} is not divisible by 5.")
    
    