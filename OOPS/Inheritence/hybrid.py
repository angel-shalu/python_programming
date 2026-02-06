"""Combination of more than one inheritance is called hybrid.

Hybrid inheritance = combination of two or more inheritance types
(Mostly: Multiple + Multilevel)"""

class Person:
    def role(self):
        print("I am a person")

class Employee(Person):
    def job(self):
        print("I am an employee")

class Student(Person):
    def study(self):
        print("I am a student")

class Intern(Employee, Student):
    def work(self):
        print("I am an intern")


i = Intern()
i.role()
i.job()
i.study()
i.work()
