"""
frozenset Python ka ek built-in data type hai jo set jaisa hota hai, lekin immutable hota hai.
Iska matlab hai ki ek baar frozenset ban jaane ke baad, hum usme naye elements add nahi kar sakte,
existing elements ko remove nahi kar sakte, ya unhe modify nahi kar sakte.

Frozenset ka use tab kiya jata hai jab hume ek aisa collection chahiye hota hai jisme elements change na ho sakein,

Simple words me:
frozenset = set ka fixed (frozen) version
Jo banne ke baad change nahi hota

fs = frozenset([1, 2, 3, 4])
print(fs)
# Output: frozenset({1, 2, 3, 4})
"""

lst = [10, 20, 30, 20]
fs = frozenset(lst)
print(fs)


# ------------------------------------------------------
# Check karo element frozenset me hai ya nahi
fs = frozenset([1, 2, 3, 4])

if 3 in fs:
    print("Element present")
else:
    print("Element not present")
    

# -------------------------------------------------------
# Dictionary key ke roop me frozenset use karo
data = {
    frozenset(["Math", "Science"]): "Group A",
    frozenset(["English", "History"]): "Group B"
}
print(data)

