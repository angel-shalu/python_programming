"""In multiple inheritence a single child class or derived class can inherit more than one parent class or base class"""

class Class1:
    def __init__(self, name):
        self.name = name
        print("This is class 1 constructor")

    def show_class1(self):
        print("Your name :", self.name)


class Class2():
    def __init__(self, salary):
        self.salary = salary
        print("This is class 2 constructor")

    def show_class2(self):
        print("Your salary :", self.salary)
        
        
class ChildClass(Class1,Class2):
    def __init__(self, name, salary):
        Class1.__init__(self, name)
        Class2.__init__(self, salary)

    def my_func(self):
        print("Name:", self.name)
        
obj = ChildClass("Shalu", 700000)
obj.show_class1()
obj.show_class2()
"""In multiple inheritence a single child class or derived class can inherit more than one parent class or base class"""

class Class1:
    def __init__(self, name):
        self.name = name
        print("This is class 1 constructor")

    def show_class1(self):
        print("Your name :", self.name)


class Class2():
    def __init__(self, salary):
        self.salary = salary
        print("This is class 2 constructor")

    def show_class2(self):
        print("Your salary :", self.salary)
        
        
class ChildClass(Class1,Class2):
    def __init__(self, name, salary):
        Class1.__init__(self, name)
        Class2.__init__(self, salary)

    def my_func(self):
        print("Name:", self.name)
        
obj = ChildClass("Shalu", 700000)
obj.show_class1()
obj.show_class2()
