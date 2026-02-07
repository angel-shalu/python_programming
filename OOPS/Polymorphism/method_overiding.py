"""
Child class parent class ke method ko redefine karta hai
    Same method name
    Same parameters
    Inheritance compulsory
    
    NOTE:-Method overriding occurs when a child class provides a specific implementation of a method 
    already defined in its parent class.
    
    
------------Key Differences---------------

Feature	                 Overloading	Overriding

Same Method Name	        Yes	            Yes
Parameters	              Different	       Same
Inheritance Required	    No	            Yes
Python Support	          Indirect	       Fully
Runtime Polymorphism	    No	            Yes"""
    
# ==========================================================================================

class Parent:
    def show(self):
        print("This is Parent method")

class Child(Parent):
    def show(self):
        print("This is Child method")

obj = Child()
obj.show()      #Parent ka method override ho gaya
