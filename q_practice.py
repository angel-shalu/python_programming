# WAP to find the largest and second largest number in a list using if–else
ls = [45, 12, 78, 23, 89]

largest = ls[0]                             # ye phla element ko largest maan ke chalte hain
second = ls[0]                              # ye bhi phla element ko 2nd largest maan ke chalte hain

for i in ls:                                      # ye list ke har element pe iterate karega  
    if i > largest:                               # agar current element largest se bada hai
        second = largest                          # agr koi number largest mil gya to purana largest 2nd largest ban jaata hai.
        largest = i                               # aur naya element largest ban jaata hai
    elif i > second and i != largest:             # agar current element 2nd largest se bada hai aur largest ke barabar nahi hai to usko 2nd largest bana do
        second = i                                # to 2nd largest ko current element bana do 

print("Largest:", largest)
print("Second Largest:", second)
