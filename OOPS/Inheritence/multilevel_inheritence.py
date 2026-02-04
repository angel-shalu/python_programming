class Class1:
    def __init__(self, name):
        self.name=name
        print("This is class 1 constructor")

    def show_class1(self):
        print("This is class 1 function.", self.name)


class Class2(Class1):
    def __init__(self,name,salary):
        super().__init__()
        self.salary=salary
        print("This is class 2 constructor")

    def show_class2(self):
        print("This is class 2 function.",self.name, self.salary)


class Class3(Class2):
    def __init__(self,salary,account):
        super().__init__()
        self.account=account
        print("This is class 3 constructor")

    def show_class3(self):
        print("This is class 3 function",self.name, self.salary, self.account)
        
obj = Class3()
obj.show_class1()

obj1=Class2("shalu",2000000)
obj1.show_class2()

obj2=Class3()




# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("Person constructor")

#     def show_name(self):
#         print(f"Name: {self.name}")


# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary
#         print("Employee constructor")

#     def show_salary(self):
#         print(f"Salary: {self.salary}")


# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#         print("Manager constructor")

#     def show_department(self):
#         print(f"Department: {self.department}")

# obj = Manager("Shalu", 700000, "IT")

# obj.show_name()              # from Person
# obj.show_salary()            # from Employee
# obj.show_department()        # from Manager
