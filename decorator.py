# """When we pass function as an argument in another function to extend the functionality of a function 
# and returns modified function this concept is known as decorator"""

# def decorator(func):
#     def inner(name):
#         if name == "Shalu":
#             print("She is going to clg.")
#         else:
#             func(name)        #yah pe func as a agrument pass kiye h 
#     return inner

# def myfuction(name):
#     print(f"In clg, plz attend all the lecture : {name}")
# myfuction("Shalu")
# myfuction("Shalini")


# # ----------------------------
# def decorator(func):
#     def inner(name):
#         if name == "Shalu":
#             print("She is going to clg.")
#         else:
#             func(name)        #yah pe func as a agrument pass kiye h 
#     return inner
# @decorator
# def myfuction(name):
#     print(f"In clg, plz attend all the lecture : {name}")
# myfuction("Shalu")
# myfuction("Shalini")


# # ------------------------------------
# def decorator(func):
#     def inner(name):
#         if name == "Shalu":
#             print("She is going to clg...")
#         else:
#             func(name)        #yah pe func as a agrument pass kiye h 
#     return inner

# def myfuction(name):
#     print(f"In clg, plz attend all the lecture : {name}")
# var1 = decorator(myfuction)
# var1 ("Shalu")
# myfuction("Shalini")


# ====================================================================
# DECORATOR CHAININHG
# ====================================================================

def decorator(func):
    def inner(name):
        if name == "Shalu":
            print("She is going to clg...")
        else:
            func(name)        #yah pe func as a agrument pass kiye h 
    return inner

def decorator1(func):
    def inner(name):
        if name == "Faculty":
            print("Why are you late ?", name)
        else:
            func(name)
    return inner

@decorator
@decorator1

def myfuction(name):
    print(f"In clg, plz attend all the lecture : {name}")
myfuction("Faculty")
myfuction("Shalu")
myfuction("Shalini")