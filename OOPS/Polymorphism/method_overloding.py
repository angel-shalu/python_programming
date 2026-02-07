"""
Same method name, but different number or type of parameters.

Important (Python Truth)
    Python true method overloading support nahi karta
    Last defined method overwrite ho jata hai...
    
    NOTE:-Method overloading means defining multiple methods with the same name but different parameters; 
    Python achieves this using default arguments or *args."""
    
# =========================================================
# How Python Handles Overloading (Using Default Arguments)

class Math:
    def add(self, a, b, c=0):
        print(a + b + c)

m = Math()
m.add(2, 3)
m.add(2, 3, 4)



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
