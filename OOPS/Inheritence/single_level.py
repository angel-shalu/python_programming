class parent:
    x = 100
class child(parent):
    pass
obj = child
print(obj.x)



# ==================================
class A:
    def funA(self):
        print("Class A")

class B(A):
    def funB(self):
        print("Class B")

obj = B()
obj.funA()
obj.funB()

# ========================================
class Parent:
    def __init__(self, name):
        self.name=name
    def parent_func(self):
        print(f"Your name = {self.name}")
class Child:
    def __init__(self,salary):
        self.salary=salary
        print("Child constructor")
    def child_func(self):
        print(f"Your salary = {self.salary}")
obj=Child(700000)
obj.child_func()
        

# ===================================================================    
"""        SUPER METHOD
To inherit the properties of parent class constructor then we can use super method inside the child class constructor"""
# ====================================================================

class Parent:
    def __init__(self, name):
        self.name = name
        print("This is parent constructor.")

    def parent_func(self):
        print(f"Your name = {self.name}")

class Child(Parent):                        # Inheriting Parent
    def __init__(self, name, salary):
        super().__init__(name)              # calls Parent constructor
        self.salary = salary
        print("Child constructor")

    def child_func(self):
        print(f"Your salary = {self.salary} and Name = {self.name}")


obj = Child("Shalu", 700000)
obj.child_func()
obj.parent_func()




#
"""When we declare more than one function which having same name but passing parameter is different
    then it is called function overloding
    
    NOTE :- Due to dynamically type of python python can not support function overloading."""
    
def my_func(a):
    print("Thid is my_function 1 ")
def my_func(b):
    print("Thid is my_function 2 ")
class parent:
    x = 100
class child(parent):
    pass
obj = child
print(obj.x)



# ==================================
class A:
    def funA(self):
        print("Class A")

class B(A):
    def funB(self):
        print("Class B")

obj = B()
obj.funA()
obj.funB()

# ========================================
class Parent:
    def __init__(self, name):
        self.name=name
    def parent_func(self):
        print(f"Your name = {self.name}")
class Child:
    def __init__(self,salary):
        self.salary=salary
        print("Child constructor")
    def child_func(self):
        print(f"Your salary = {self.salary}")
obj=Child(700000)
obj.child_func()
        

# ===================================================================    
"""        SUPER METHOD
To inherit the properties of parent class constructor then we can use super method inside the child class constructor"""
# ====================================================================

class Parent:
    def __init__(self, name):
        self.name = name
        print("This is parent constructor.")

    def parent_func(self):
        print(f"Your name = {self.name}")

class Child(Parent):                        # Inheriting Parent
    def __init__(self, name, salary):
        super().__init__(name)              # calls Parent constructor
        self.salary = salary
        print("Child constructor")

    def child_func(self):
        print(f"Your salary = {self.salary} and Name = {self.name}")


obj = Child("Shalu", 700000)
obj.child_func()
obj.parent_func()




#
"""When we declare more than one function which having same name but passing parameter is different
    then it is called function overloding
    
    NOTE :- Due to dynamically type of python python can not support function overloading."""
    
def my_func(a):
    print("Thid is my_function 1 ")
def my_func(b):
    print("Thid is my_function 2 ")
my_func(777)
