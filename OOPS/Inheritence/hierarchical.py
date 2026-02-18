"""When a parent class can be inherited by more than one child class.
    Ek hi Parent class se multiple Child classes inherit karti hain."""

"""In multiple inheritence a single child class or derived class can inherit more than one parent class or base class."""

class Class1:
    def __init__(self, name):
        self.name = name
        print("This is class 1 constructor")

    def show_class1(self):
        print("Your name :", self.name)


class Class2(Class1):
    def __init__(self, name):
        super().__init__(name)
        print("This is class 2 constructor")

    def show_class2(self):
        print("Your Name :", self.name)
        
        
class ChildClass(Class1):
    def __init__(self, name, salary):
        Class1.__init__(self, name)
        
    def my_func(self):
        print("Name:", self.name)
        
obj = Class2("Shalu")
obj.show_class2()



# ==============================================================
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")


d = Dog()
d.sound()
d.bark()

c = Cat()
c.sound()
c.meow()
