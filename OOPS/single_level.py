class parent:
    x = 100
class child(parent):
    pass
obj = child
print(obj.x)



# ==================================
class A:
    def funA(self):
        print("Class A")

class B(A):
    def funB(self):
        print("Class B")

obj = B()
obj.funA()
obj.funB()
