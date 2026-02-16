# def my_generator():
#     yield "A"
#     yield "B"
#     yield "C"
    
# g = my_generator()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))

# # ==========================================================================
# # WAP to generate countdown 5,4,3,2,1 using generator function
# # ==========================================================================

# def countdown_generator(num):
#     print("Time start")
#     while (num>=0):
#         yield num
#         num=num-1
# var = countdown_generator(10)
# print(var)
# for i in var:
#     print(i)
    
# # ========================================================================

# def count_down(num):
#     print("Countdown started")
#     while (num>=0):
#         yield num
#         num=num-1
# var = count_down(int(input("Enter the number : ")))
# print(var)
# for i in var:
#     print(i)
    
    
#=============================================================================
def count_up(num):
    while num <= 10:
        yield num
        num += 1

var = count_up(int(input("Enter the number : ")))
print(var)
for i in count_up(1):
    print(i)

