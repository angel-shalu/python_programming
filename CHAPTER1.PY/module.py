"""
1. MODULE:- Module is a file containing code written by someone else which can be imported and used in our program
PIP :- it is a package manager for python.You can use to pip to install module on your system.

Type of module
1. Built in module
2. External module 

USINHG PYTHON AS A CALCULATOR:
We can use python as a calculator by typing python on the terminal
This opens REPL or [Read Evaluate Print Loop]

By using triple quote and triple double quote u can print multiple line 
or comment the multiple lines also

"""

import pyjokes 
# this prints a random joke
joke=pyjokes.get_joke()
print(joke)