<<<<<<< HEAD
# def diamond_pattern(n):
#     for i in range(0,n):
#         for j in range(0, n-i-1):
#             print(" ", end="")
#         for j in range(0, i+1):
#             print("*", end=" ")
#         print()
        
# # lower part
#     for i in range(0, n-1):
#         for j in range(0,i+1):
#             print(" ", end="")
#         for j in range(0, n-i-1):
#             print("*", end=" ")
#         print()
# diamond_pattern(5)



# # ======================================================
# n = int(input("Enter the number of rows :"))
# # for rows
# for i in range(1,n+1):
    
#     # for space printing
#     for j in range(n-i, 0, -1):
#         print(" ", end="")
        
#     # for for star printing
#     for j in range(1, i+1):
#         print("*", end=" ")
        
#     # for new line
#     print()
        
# # lower part
# for i in range(1, n):
#     for j in range(1,i+1):                 
#         print(" ", end="")
#     for j in range(n-i, 0, -1):
#         print("*", end=" ")
#     print()
    
    

# =======================================
# HOLLOW DIAMOND
# =======================================
n = int(input("Enter the number of rows : "))

# ---------- Upper Part ----------
for r in range(1, n+1):

    # spaces
    for s in range(n-r, 0, -1):
        print(" ", end="")

    # stars
    for p in range(1, r+1):
        if r == 1:
            print("* ", end="")
        else:
            if p == 1 or p == r:
                print("* ", end="")
            else:
                print("  ", end="")
    print()

# ---------- Lower Part ----------
for r in range(n-1, 0, -1):

    # spaces
    for s in range(n-r):
        print(" ", end="")

    # stars
    for p in range(1, r+1):
        if p == 1 or p == r:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
=======
# def diamond_pattern(n):
#     for i in range(0,n):
#         for j in range(0, n-i-1):
#             print(" ", end="")
#         for j in range(0, i+1):
#             print("*", end=" ")
#         print()
        
# # lower part
#     for i in range(0, n-1):
#         for j in range(0,i+1):
#             print(" ", end="")
#         for j in range(0, n-i-1):
#             print("*", end=" ")
#         print()
# diamond_pattern(5)



# # ======================================================
# n = int(input("Enter the number of rows :"))
# # for rows
# for i in range(1,n+1):
    
#     # for space printing
#     for j in range(n-i, 0, -1):
#         print(" ", end="")
        
#     # for for star printing
#     for j in range(1, i+1):
#         print("*", end=" ")
        
#     # for new line
#     print()
        
# # lower part
# for i in range(1, n):
#     for j in range(1,i+1):                 
#         print(" ", end="")
#     for j in range(n-i, 0, -1):
#         print("*", end=" ")
#     print()
    
    

# =======================================
# HOLLOW DIAMOND
# =======================================
n = int(input("Enter the number of rows : "))

# ---------- Upper Part ----------
for r in range(1, n+1):

    # spaces
    for s in range(n-r, 0, -1):
        print(" ", end="")

    # stars
    for p in range(1, r+1):
        if r == 1:
            print("* ", end="")
        else:
            if p == 1 or p == r:
                print("* ", end="")
            else:
                print("  ", end="")
    print()

# ---------- Lower Part ----------
for r in range(n-1, 0, -1):

    # spaces
    for s in range(n-r):
        print(" ", end="")

    # stars
    for p in range(1, r+1):
        if p == 1 or p == r:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
>>>>>>> edc38913634259038058ced79e7e8598d76e3cae
