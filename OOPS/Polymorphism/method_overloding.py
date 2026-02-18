"""
METHOD OVERLOADING.................

Same method name, but different number or type of parameters.

Important (Python Truth)
    Python true method overloading support nahi karta
    Last defined method overwrite ho jata hai...
    
NOTE:-Method overloading means defining multiple methods with the same name but different parameters; 
    Python achieves this using default arguments or *args.
    
    
    
In python there will be a two type of method overloading 
    1. Function Overloading
    2. Constructor Overloading
    
    But due do dynamically type python does not support method overloading 
    but python will always consider only last method"""
    
# =========================================================
# How Python Handles Overloading (Using Default Arguments)
# =========================================================

class my_cls:
    def my_func(a):
        print(a)
    def my_func(a,b):
        print(f"a = {a} and b = {b}")

obj = my_cls()
obj.my_func(2,3)




# =========================================

class Math:
    def add(self, a, b, c=0):
        print(a + b + c)

m = Math()
m.add(2, 3)
m.add(2, 3, 4)

# =========================================================



# ==============================================
# using *args
class Math:
    def add(self, *args):
        total = 0
        for i in args:
            total += i
        print(total)

m = Math()
m.add(2, 3)
m.add(2, 3, 4, 5)
