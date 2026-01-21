"""When the large program can be divided into sub programs and these sub programs is content a block of code that perform a specific task.
These block of code are called functions.

Functions can be used again and agin.

# ---------------------------------------------------------------------------------
TYES OF FUNCTIONS
1. Built-in functions / Pre-defined functions
Built-in functions: jo python me pre-defined hoti hai jaise print(), input(), len() etc.
These functions are already declared in python and we can use them directly.

2. User-defined functions
User-defined functions: jo hum khud banate hai apne program ke liye.
    1. No return type and no argument / parameter
    2. No return but argument / parameter
    3. Return without argument / parameter
    4. Return with argument / parameter

3. Anonymous functions / Lambda functions
Anonymous functions: jo bina naam ke hoti hai aur ek line me hi likhi jati hai.

# ---------------------------------------------------------------------------------
Syntax of function:
def function_name():
    statement1
    statement2
    
-------------------------------------------------------------------------------------
Types of variables in function you can create when declaring function:
-------------------------------------------------------------------------------------
1. Local variable: jo function ke andar declare hota hai aur sirf usi function ke andar use hota hai.
    When we define the function inside the function then it is called local variable.
    The scope of local variable is available only inside the function.

2. Global variable: jo function ke bahar declare hota hai aur pure program me kahi bhi use hota hai.
    When we define the function outside the function then it is called local variable.
    The scope of local variable is available inside the function as well as outside the function.
    
# ---------------------------------------------------------------------------------
 """
# ------------------ NO RETURN TYPE AND NO ARGUMENT / PARAMETER ------------------
def my_function():
    print("Hello from a function")  
my_function()          # function call

# ---------------------------------------------------------
# Local variable example
def add():
    a = 10
    b = 20
    c = a + b
    print(a)
    print("Addition =", c)
add()                  # function call

# # ---------------------------------------------------------
# def addition():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     sum = num1 + num2
#     print("Sum =", sum)
# addition()             # function call

# ----------------------------------------------------------
# Global variable example
a = 50                 # global variable
def add():
    a = 10
    b = 20
    c = a + b
    print(a)                  # prints local variable a
    print("Addition =", c)
add()                  # function call
print("Value of a outside function:", a)              # prints global variable a