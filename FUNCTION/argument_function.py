"""TYPES OF ARGUMENT
    Positional Argument 
    Keyword 
    Default
    Variable Length
    Arbtrary """
    
    
# Positional Argument
def argument_function1(x,y):
    print(x, " ", y)
argument_function1(10,20)


# ----------------Keyword Argument------------------------
def argument_function2(name, age):
    print(age,name)
argument_function2(age= 20, name="shalu")


# -----------------Default Argument-----------------------
def argument_function3(name="shalu"):
    print(name)
argument_function3("shalini")


# -------------Variable Length Argument-----------------
def argument_function4(*n):                        
    total = 0
    for i in n:
        total = total + i                  
    print(total)
argument_function4()                               # output: 0
argument_function4(6)                              # output: 6  
argument_function4(10,20)                          # output: 30

# ------------------Arbitrary Argument-----------------------
def argument_function4(*n):
    total = 0
    for i in n:
        total = total + i
    print(total)

def argument_function5(**n1):
    print(type(n1))
    print(n1)

    for k,v in n1.items():
        print(f"key={k} and value={v}")

argument_function4()
argument_function4(6)
argument_function4(10,20)

argument_function5()
argument_function5(name="shalu", age=20, city="delhi")