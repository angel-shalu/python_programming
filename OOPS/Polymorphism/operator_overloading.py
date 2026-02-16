<<<<<<< HEAD
"""Operator overloading means we can use operator and method for different purposes.

    NOTE :- We can not overload the object of a class.
      but python have built in magic methods in which we can overload the other operations.
    """

print(20+40)
print("Hello"+"World")


# ============================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __add__(self, other):
        return self.my_var+other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Sum = " ,Obj1 + Obj2)
      
      
# =====================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __sub__(self, other):
        return self.my_var - other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Sub = ",Obj1 - Obj2)


# =========================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __mul__(self, other):
        return self.my_var * other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Multiple = ",Obj1 * Obj2)


# =======================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __truediv__(self, other):
        return self.my_var / other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Div = ", Obj1 / Obj2)



# =======================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __floordiv__(self, other):
        return self.my_var // other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Floor Div = ", Obj1 // Obj2)


# =======================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __mod__(self, other):
        return self.my_var % other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Modulus = ", Obj1 % Obj2)





# --------------------------------------------------------------------------
"""NOTE :- We can also overload the relational operator using magic method."""
# --------------------------------------------------------------------------

class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __gt__(self, other):
        return self.my_var > other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Obj1 is greater than Obj2 = ", Obj1 > Obj2)






# ===========================================================================================
# WAP TO CREATE A TWO DIOFFERENT CLASS AND MULTIPLE THIS TWO CLASS OBJECT USING MAGICE METHOD
# ===========================================================================================
class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        
    def __mul__(self, other):
        return self.salary*other.days
    
class Employee_Detail:
    def __init__(self, name, days):
        self.name = name
        self.days = days
        
Employee = Employee("Shalu",50000)
Detail = Employee_Detail("Shalu",25)
print("Multiple of TWO class = ", Employee * Detail)

    
=======
"""Operator overloading means we can use operator and method for different purposes.

    NOTE :- We can not overload the object of a class.
      but python have built in magic methods in which we can overload the other operations.
    """

print(20+40)
print("Hello"+"World")


# ============================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __add__(self, other):
        return self.my_var+other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Sum = " ,Obj1 + Obj2)
      
      
# =====================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __sub__(self, other):
        return self.my_var - other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Sub = ",Obj1 - Obj2)


# =========================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __mul__(self, other):
        return self.my_var * other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Multiple = ",Obj1 * Obj2)


# =======================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __truediv__(self, other):
        return self.my_var / other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Div = ", Obj1 / Obj2)



# =======================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __floordiv__(self, other):
        return self.my_var // other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Floor Div = ", Obj1 // Obj2)


# =======================================
class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __mod__(self, other):
        return self.my_var % other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Modulus = ", Obj1 % Obj2)





# --------------------------------------------------------------------------
"""NOTE :- We can also overload the relational operator using magic method."""
# --------------------------------------------------------------------------

class my_cls:
    def __init__(self, my_var):
        self.my_var = my_var
    def __gt__(self, other):
        return self.my_var > other.my_var
Obj1 = my_cls(100)
Obj2 = my_cls(200)
print("Obj1 is greater than Obj2 = ", Obj1 > Obj2)






# ===========================================================================================
# WAP TO CREATE A TWO DIOFFERENT CLASS AND MULTIPLE THIS TWO CLASS OBJECT USING MAGICE METHOD
# ===========================================================================================
class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        
    def __mul__(self, other):
        return self.salary*other.days
    
class Employee_Detail:
    def __init__(self, name, days):
        self.name = name
        self.days = days
        
Employee = Employee("Shalu",50000)
Detail = Employee_Detail("Shalu",25)
print("Multiple of TWO class = ", Employee * Detail)

    
>>>>>>> edc38913634259038058ced79e7e8598d76e3cae
