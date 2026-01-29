# num = int(input("Enter the number of rows :"))
# for i in range(0, num):
#     for j in range(0, num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print()
    

# # ----------2nd logic----------
# num = int(input("Enter the number of rows: "))
# for i in range(1, num+1):
#     # spaces
#     for j in range(num - i):
#         print(" ", end="")
#     # stars
#     for j in range(1, i+1):
#         print("* ", end="")
#     print()
    

# # -----------------------------
# # SINGLE LOOP 
# # ------------------------------
# def pyramid_pattern(rows):
#     for i in range(rows):
#         print(""*(rows-i-1)+"*"(i+1))
# pyramid_pattern(5)
              
              
# # ==================================
# # 2nd method using function
# # ==================================
# def pyramid_pattern(num):
#     for i in range(0, num):
#         for j in range(0, num-i-1):
#             print(end=" ")
#         for j in range(0,i+1):
#             print("*", end=" ")
#         print()
# pyramid_pattern(5)




# # ----------------------------
# # EVEN NUMBER OF STAR
# #---------------------------------
# num = int(input("Enter the number of rows :"))
# for i in range(1, num+1):
#     for j in range(num-i):
#         print(end="  ")
#     for j in range(1,2*i+1):
#         print("*", end=" ")
#     print()

# # USING DUNCTION----------
# def even_pyramid_pattern(num):
#     for i in range(1, num+1):
#         for j in range(num-i):
#             print(end="  ")
#         for j in range(1,2*i+1):
#             print("*", end=" ")
#         print()
# even_pyramid_pattern(7)

# # -----------------------------
# # SINGLE LOOP 
# # ------------------------------
# def pyramid_pattern(rows):
#     for i in range(rows):
#         print(""*(rows-i-1)+"*"(2*i+1))
# pyramid_pattern(5)
              





# # ==========================================================================
# # REVERSE PATTERN
# # ===========================================================================
# def reverse_pyramid(num):
#     for i in range (num, 0, -1):
#         for j in range(0, num-i):
#            print(end=" ") 
#         for j in range(0, i):
#             print("*", end=" ")
#         print()
# reverse_pyramid(6)


# # 2nd logic----------------
# def reverse_pyramid(num):
#     for i in range (num, 1, -1):
#         for j in range(1, num-i+1):
#            print(end=" ") 
#         for j in range(1, i):
#             print("*", end=" ")
#         print()
# reverse_pyramid(6)

# ------------------------------


