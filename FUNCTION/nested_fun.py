"""When we declare a function insinde anyothe function then it is called nested function"""

def outer():
    print("This is outer function")
     
    def inner():
        print("This is inner function")
    
    print("Outer function finish")
outer()

# ----------------------------------------
def outer():
    print("This is outer function")
     
    def inner():
        print("This is inner function")
    inner()
    
    print("Outer function finish")
outer()



# --------------------------------
def outer():
    print("This is outer function")
     
    def inner(x,y):
        z = x+y
        print("This is inner function = ", z)
    x1 = int(input("Enter the frist number : "))
    y1 = int(input("Enter the second number : "))
    inner(x1, y1)
    
    print("Outer function finish")
outer()
"""When we declare a function insinde anyothe function then it is called nested function"""

def outer():
    print("This is outer function")
     
    def inner():
        print("This is inner function")
    
    print("Outer function finish")
outer()

# ----------------------------------------
def outer():
    print("This is outer function")
     
    def inner():
        print("This is inner function")
    inner()
    
    print("Outer function finish")
outer()



# --------------------------------
def outer():
    print("This is outer function")
     
    def inner(x,y):
        z = x+y
        print("This is inner function = ", z)
    x1 = int(input("Enter the frist number : "))
    y1 = int(input("Enter the second number : "))
    inner(x1, y1)
    
    print("Outer function finish")
outer()
