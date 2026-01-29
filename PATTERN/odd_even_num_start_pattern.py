# ODD NUMBER STAR PATTERN
num = int(input("Enter the number of rows :"))
k = 1
for i in range(1, num+1):
    for j in range(1, k+1):
        print("*", end=" ")
    k += 2
    print()
        


# EVEN NUMBER STAR PATTERN   
num = int(input("Enter the number of rows :"))
k = 2
for i in range(1, num+1):
    for j in range(1, k+1):
        print("*", end=" ")
    k += 2
    print()      
