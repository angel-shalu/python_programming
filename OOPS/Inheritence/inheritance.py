"""Inhenritance is one of distinct features of OOPs
	======Ek class dusri class ke properties (data + methods) ko use kar sake=====

=>The purpose of Inheritance is that 
" To build Re-usable Applications with Effective Memmory Management in Python Object Oriented  Programming".

    1.						Types of Inheritances OR Re-usbale Tech in Python
				=========================================================
=>Types of Inheritance is one of the Model / Diagram / Pattern which makes us to understand How the Features are Inherited from  Base Class to Dervied Class.
=>In Python Programming, we have 5 Types of Inheritances. They are
			1. Single Inheritance
			2. Multi Level Inheritance
            3. Multiple Inheritance
			4. Hierarchical Inheritance
			5. Hybrid Inheritance
"""

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

c = Child()
c.show()      # Parent ka method
c.display()   # Child ka method
