"""
Sometime we can declare a function without name such type of function is known as anonymous function.
These function have a purpose of instant use.

"""

#  Lambda Function :- It is a single line function which have return type 
s = lambda a : a*a
print(s(7))

s1 = lambda a,b : a+b
print(s1(10,20))

s2 = lambda x, y : x if x > y else y
print(s2(20,30))


# -----------------------------------------------------------
#   Filter Function : - We can use filter function to filtter value from any give sequence following by condition
# --------------------------------------------------------------

def Iseven(x):
    if x % 2==0:
        return True
    else:
        False
l = [ 2, 5, 6, 7, 9, 4]
print(filter(Iseven,l))
l1 = list(filter(Iseven,l))
print(l1)

# 2nd method by using lambda
l2 = list(filter(lambda x: x%2==0,l))
print(l2)



# =====================================================================================================
# WAP to find all thr prime number from the given sequence 2, 3, 4, 5, 6, 7, 8, 9 using filter function
# =====================================================================================================

nums = [2, 3, 4, 5, 6, 7, 8, 9]

# function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# using filter function
prime_numbers = list(filter(is_prime, nums))
print("Prime numbers:", prime_numbers)

# --------------------------------------------
# 2nd method
def prime_num(x):
    i = 1
    count = 0
    while(i<=x):
        if(x%i==0):
            count+=1
        i+=1
    if count == 2:
        return True
l = [2, 3, 4, 5, 6, 7, 8, 9]
l1 = list(filter(prime_num,l))
print(l1)



# ----------------------------------------------------------------------------
nums = [2, 3, 4, 5, 6, 7, 8, 9]
primes = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, n)), nums))
print(primes)

