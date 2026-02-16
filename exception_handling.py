""" EXCEPTION HANDING AND FILE HANDLING


In any programming language, there will be a TWO types of error possible.
    1. Syntax error 
    2. Runtime error
    
"""
# ==============================================================
# 1. Syntax error :- This error occurs bcoz of invalid syntax.
# ==============================================================
# x = 7
# if x==7
#     print(7)
    
    
# ==============================================================
"""  2. Runtime error :- This error is also known as exception.

    TYPES OF RUNTIME ERROR 
    1. ZeroDivision Error
    2. Value Error
    3. Type error
    4. File Not Found Error
    5. End of file error 
    6. type puncher error
    7. sleeping error """
# ==============================================================

""" How to handle exception or runtim,e error in python ?
    ------> We can handle runtime error using try and except block.
"""
# try:
#     x = int(input("Enter the firt number :"))
#     y = int(input("Enter the seocnd number :"))
#     print(x/y)
# except:
#     print("Any number can not be divide by zero.")


# # ================================================================
# try:
#     x = int(input("Enter the firt number :"))
#     y = int(input("Enter the seocnd number :"))
#     print(x/y)
    
# except ZeroDivisionError:
#     print("Any number can not be divide by zero.")
    
# except ValueError:
#     print("Put the number in the form of integer")
    
    
# # ================================================================
# #             MULTIPLE EXCEPT ERRRO
# # ==================================================================
# try:
#     x = int(input("Enter the firt number :"))
#     y = int(input("Enter the seocnd number :"))
#     print(x/y)
    
# except ZeroDivisionError:
#     print("Any number can not be divide by zero.")
    
# except ValueError:
#     print("Put the number in the form of integer")
    
# finally:
#     print("Program close.... Thanks")


# # ===================================================================
# # APPROCH 2
# # ===================================================================

# try:
#     x = int(input("Enter the firt number :"))
#     y = int(input("Enter the seocnd number :"))
#     print(x/y)
    
# except (ZeroDivisionError, ValueError) as msg:
#     print("Error = ", msg)
    
# ===================================================================
    
    
""" FINALLY BLOCK :-  Finally block can execute as a program have runtime error or not..

    DEFAULT EXCEPT BLOCK :- This can except all type of error.
    NOTE:- But it is necessary default except block written in last."""
    
# ===================================================================
# APPROCH 3
# ===================================================================
try:
    x = int(input("Enter the firt number :"))
    y = int(input("Enter the seocnd number :"))
    print(x/y)
except ZeroDivisionError:
    print("Not divide by zero")
except :
    print("Value is wrong...")
    
    
# =========================================================================
# TRY, EXCEPT AND ELSE
# =========================================================================
try:
    x = int(input("Enter the firt number :"))
    y = int(input("Enter the seocnd number :"))
    print(x/y)
except ZeroDivisionError:
    print("Not divide by zero")
except :
    print("Value is wrong...")
else:
    print(x/y)
    
    
# ===========================================================================
"""TYPES OF EXCEPTIONS :-
    In python, there will be a two types of exception..
    1. Pre-Defined Exceptions
	2. User Defined Exceptions"""