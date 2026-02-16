"""The general Notation of Complex Number OR Value is shown Bellow.
				a+bj   OR  a-bj
		=>Here 'a' is called Real Part
		=>here 'b' is called Imaginary Part
"""
a = 2 + 7j
print(a)  # Output: (2+7j)
print(type(a))  # Output: <class 'complex'>
print(a,(type(a)))  # Output: (2+7j) <class 'complex'>

a=2+3j #Here '2' is Real Part and '3' is Imaginary Part
b=5-7j #Here '5' is Real Part and '7' is Imaginary Part
print("Complex Number a:",a)  # Output: Complex Number a: (2+3j)
print("Complex Number b:",b)  # Output: Complex Number b: (5-7j)

#Accessing Real Part and Imaginary Part
print("Real Part of a:",a.real)  # Output: Real Part of a: 2.0
print("Imaginary Part of a:",a.imag)  # Output: Imaginary Part of a: 3.0
print("Real Part of b:",b.real)  # Output: Real Part of b: 5.0
print("Imaginary Part of b:",b.imag)  # Output: Imaginary Part of b: -7.0

#Arithmetic Operations on Complex Numbers
a = 2 + 3j
b = 5 - 7j
print("Addition of a and b:",a+b)  # Output: Addition of a and b: (7-4j)
print("Subtraction of a and b:",a-b)  # Output: Subtraction of a and b: (-3+10j)
print("Multiplication of a and b:",a*b)  # Output: Multiplication of a and b: (31+1j)
print("Division of a by b:",a/b)  # Output: Division of a by b: (-0.17073170731707318+0.5365853658536586j)

#Conjugate of a Complex Number


