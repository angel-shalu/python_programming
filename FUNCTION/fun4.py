def myfunction(x,y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    fdiv = x // y
    rem = x % y
    power = x ** y
    
    return add, sub, mul, div, fdiv, rem, power
z= myfunction(20,10)
for i in z:
    print(i)