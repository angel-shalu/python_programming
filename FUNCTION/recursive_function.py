"""When a function automatically calls itself is called recursive function.
It is used to solve problems that can be broken down into smaller, similar subproblems.

----------In recursive function, there are two main conditions-----------:
1. Base Case: This is the condition under which the recursion stops. It prevents infinite recursion and eventual stack overflow.
    Function khud ko call kna band kr dega or ruk jayega jab base case pr pohnch jayega.
    
2. Recursion Case: This is where the function calls itself with a modified argument, moving towards the base case.
    Function apne aap ko call krta hai."""
    
# Example of recursive function to calculate factorial of a number
def myrecursive_function(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * myrecursive_function(n - 1)
    
    
def myrecursive_function(n):
    if n == 0:
        result = 0
    else:
        result = n + myrecursive_function(n - 1)
    return result
# Test the recursive function
answer = myrecursive_function(10)
print("Factorial of 10 is:", answer)
        