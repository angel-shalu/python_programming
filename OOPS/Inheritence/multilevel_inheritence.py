<<<<<<< HEAD
class Class1:
    def __init__(self, name):
        self.name = name
        print("This is class 1 constructor")

    def show_class1(self):
        print("This is class 1 function.", self.name)


class Class2(Class1):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print("This is class 2 constructor")

    def show_class2(self):
        print("This is class 2 function.", self.name, self.salary)


class Class3(Class2):
    def __init__(self, name, salary, account):
        super().__init__(name, salary)
        self.account = account
        print("This is class 3 constructor")

    def show_class3(self):
        print("This is class 3 function.", self.name, self.salary, self.account)


# object creation
obj = Class1("shalu")
obj.show_class1()
print("-"*50)

obj1 = Class2("shalu", 2000000)
obj1.show_class2()
print("-"*50)

obj2 = Class3("shalu", 7000000, 12345)
obj2.show_class3()
obj2.show_class2()
obj2.show_class1()



# ======================================================
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")

    def show_name(self):
        print(f"Name: {self.name}")


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print("Employee constructor")

    def show_salary(self):
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        print("Manager constructor")

    def show_department(self):
        print(f"Department: {self.department}")

obj = Manager("Shalu", 700000, "IT")

obj.show_name()              # from Person
obj.show_salary()            # from Employee
obj.show_department()        # from Manager
=======
class Class1:
    def __init__(self, name):
        self.name = name
        print("This is class 1 constructor")

    def show_class1(self):
        print("This is class 1 function.", self.name)


class Class2(Class1):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print("This is class 2 constructor")

    def show_class2(self):
        print("This is class 2 function.", self.name, self.salary)


class Class3(Class2):
    def __init__(self, name, salary, account):
        super().__init__(name, salary)
        self.account = account
        print("This is class 3 constructor")

    def show_class3(self):
        print("This is class 3 function.", self.name, self.salary, self.account)


# object creation
obj = Class1("shalu")
obj.show_class1()
print("-"*50)

obj1 = Class2("shalu", 2000000)
obj1.show_class2()
print("-"*50)

obj2 = Class3("shalu", 7000000, 12345)
obj2.show_class3()
obj2.show_class2()
obj2.show_class1()



# ======================================================
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor")

    def show_name(self):
        print(f"Name: {self.name}")


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print("Employee constructor")

    def show_salary(self):
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        print("Manager constructor")

    def show_department(self):
        print(f"Department: {self.department}")

obj = Manager("Shalu", 700000, "IT")

obj.show_name()              # from Person
obj.show_salary()            # from Employee
obj.show_department()        # from Manager
>>>>>>> edc38913634259038058ced79e7e8598d76e3cae
