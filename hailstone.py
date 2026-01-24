"""Hailstone asal me Collatz Sequence / Collatz Conjecture se related term hai.
   Programming me jab hum kisi number se ek special rule follow karke sequence banate hain, usko Hailstone sequence kehte hain.

# ----------Hailstone Sequence ka rule--------------------
    Maan lo number n hai:
    Agar n even hai → n / 2
    Agar n odd hai → 3n + 1

👉 Ye steps tab tak repeat karte hain jab tak number 1 na ban jaye.

Example (n = 10)
    10 (even) → 10/2 = 5
    5  (odd)  → 3×5 + 1 = 16
    16 (even) → 16/2 = 8
    8  (even) → 8/2 = 4
    4  (even) → 4/2 = 2
    2  (even) → 2/2 = 1

Hailstone Sequence:
10 → 5 → 16 → 8 → 4 → 2 → 1"""


n = int(input("Enter a number: "))
print(n, end=" ")
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print("→", n, end=" ")



# # WAP to generate the hailstone sequence (Collatz sequence) for a given number n
ls = []
def hailstone_sequence(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
        ls.append(n)
hailstone_sequence(10)
print(ls)
