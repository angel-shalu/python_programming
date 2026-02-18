# ZERO ARGUMENT CONSTRUCTOR
# ---------------------------
class my_class:
    def __init__(self):
        print("This is a constructor.")
    def user_func():
        print("This is user define function.")
obj=my_class

# ------------------------------------

class my_class:
    def __init__(self,a):
        self.a = 10
        print("This is a constructor.")
    def user_func():
        print("This is user define function.")
obj=my_class(100)

# ------------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        print("This is a constructor.")
    def user_func():
        print("This is user define function.")
obj=my_class(100)

# ---------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        b=10
        print("This is a constructor.",self.a)
    def user_func(self):
        print("This is user define function.",self.a)
obj=my_class(100)
obj.user_func()

# -------------------------------
# ONCE ARGUMENT CONSTRUCTOR
# --------------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        b=10
        print("This is a constructor.",self.a)
    def user_func(self):
        self.a =500
        print("This is user define function.",self.a)
obj=my_class(100)
obj.user_func()


# ------------------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        self.b = 10
        print("This is a constructor.",self.a,self.b)
    def user_func(self):
        self.a =500
        print("This is user define function.",self.a, self.b)
obj=my_class(100)
obj.user_func()


# ======================================================
# WAP to find sum of 1 to 100 using class and function.
# ======================================================
# ZERO ARGUMENT CONSTRUCTOR
# ---------------------------
class my_class:
    def __init__(self):
        print("This is a constructor.")
    def user_func():
        print("This is user define function.")
obj=my_class

# ------------------------------------

class my_class:
    def __init__(self,a):
        self.a = 10
        print("This is a constructor.")
    def user_func():
        print("This is user define function.")
obj=my_class(100)

# ------------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        print("This is a constructor.")
    def user_func():
        print("This is user define function.")
obj=my_class(100)

# ---------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        b=10
        print("This is a constructor.",self.a)
    def user_func(self):
        print("This is user define function.",self.a)
obj=my_class(100)
obj.user_func()

# -------------------------------
# ONCE ARGUMENT CONSTRUCTOR
# --------------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        b=10
        print("This is a constructor.",self.a)
    def user_func(self):
        self.a =500
        print("This is user define function.",self.a)
obj=my_class(100)
obj.user_func()


# ------------------------------------
class my_class:
    def __init__(self,a):
        self.a = a
        self.b = 10
        print("This is a constructor.",self.a,self.b)
    def user_func(self):
        self.a =500
        print("This is user define function.",self.a, self.b)
obj=my_class(100)
obj.user_func()


# ======================================================
# WAP to find sum of 1 to 100 using class and function.
# ======================================================
