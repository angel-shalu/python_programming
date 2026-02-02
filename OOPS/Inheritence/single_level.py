class parent:
    x = 100
class child(parent):
    pass
obj = child
print(obj.x)