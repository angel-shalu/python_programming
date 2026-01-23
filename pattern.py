# # # RIGHT ANGLE TRAINGELE PATTERN
# # def my_function(x):
# #     print("This is  a right angle trainglepattern program")
# #     for i in range(x):
# #         for j in range(i+1):
# #             print("*", end=" ")
# #         print()
# # my_function(5)


# # # ======================================================================================
# # def my_function(x):
# #     print("This is  a right angle traingle pattern program")
# #     for i in range(1, x+1):
# #         for j in range(1, x+1-i):
# #             print(" ", end=" ")
# #         for k in range(1, i+1):
# #             print("*", end=" ")
# #         print()
# # my_function(5)
    
    
# # # ======================================================================================
# # # TRIANGLE PATTERN
# # def my_function(x):
# #     print("This is  a  triangle pattern program")
# #     for i in range(1, x+1):
# #         for j in range(1, x+1-i):
# #             print(" ", end=" ")
# #         for k in range(1, i+1):
# #             print("*", end="   ")
# #         print()
# # my_function(5)
    

# # ======================================================================================
# # INVERTED TRIANGLE PATTERN

# def my_function(x):
#     for i in range(1, x+1):
#         for j in range(1, x+1-i):
#             print(" ", end=" ")
#         for k in range(1, i+1):
#             print("*", end="   ")
#         print()
# my_function(5)

# def my_function1(x):
#     for i in range(1, x+1):
#         for k in range(1, i):
#             print(" ", end=" ")
#         for j in range(1, x+2-i):
#             print("*", end="   ")
#         print()
# my_function1(5)
    
    

# ======================================================================================
# SAWASTIK PATTERN

def swastik_pattern(x):
    for i in range(1, x+1):
        for j in range(1, x+1):

            if (i == 5 and j == 5):
                print("*", end=" ")

            elif ((i == 1 and j < 5) or
                  (j == 9 and i < 5) or
                  (i == 9 and j > 5) or
                  (j == 1 and i > 5)):
                print("*", end=" ")

            else:
                print(" ", end=" ")
        print()
swastik_pattern(9)
