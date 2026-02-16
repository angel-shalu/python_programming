<<<<<<< HEAD
# =============================================================================
# Returning a multiple value of a function
# =============================================================================
"""In python, in a user define function we can return multiple value from a function"""
def myfunction(x,y):
    add = x + y
    sub = x - y
    return add, sub
z = myfunction(20,10)
print(z)


# ---------------------------------------------
def myfunction(x,y):
    add = x + y
    sub = x - y
    return add, sub
z1, z2 = myfunction(20,10)
print(z1)
=======
# =============================================================================
# Returning a multiple value of a function
# =============================================================================
"""In python, in a user define function we can return multiple value from a function"""
def myfunction(x,y):
    add = x + y
    sub = x - y
    return add, sub
z = myfunction(20,10)
print(z)


# ---------------------------------------------
def myfunction(x,y):
    add = x + y
    sub = x - y
    return add, sub
z1, z2 = myfunction(20,10)
print(z1)
>>>>>>> edc38913634259038058ced79e7e8598d76e3cae
print(z2)