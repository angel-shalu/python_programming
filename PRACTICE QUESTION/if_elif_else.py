# """Q1. Smart Login Decision System

# Input: Ek program likho jo user se:
# username
# password
# attempts

# Rules:
# Username = "admin"
# Password = "Admin@123"
# Attempts > 3 → "Account Locked"
# Correct credentials → "Login Successful"
# Else → "Invalid Credentials """

# # Solution:
# username = input("Enter username: ")
# password = input("Enter password: ")    
# attempts = int(input("Enter number of login attempts: "))
# if attempts >3:
#     print("Account Locked")
# elif username == "admin" and password == "Admin@123":
#     print("Login Successful")
# else:
#     print("Invalid Credentials")
    
    
# ============================================================================
"""Q2. Electricity Bill Generator

Input:
units

Rules:
≤ 100 → ₹0
101–200 → ₹5/unit
201–300 → ₹8/unit
300 → ₹12/unit"""

# Solution:
units = int(input("Enter number of units consumed: "))

if units <= 100:
    bill= 0
    
    """Logic:
    First 100 units → Free
    Bache hue units = units - 100
    Har unit ka rate = ₹5"""
    
elif units <= 200:                             #yaha pe 100 se jysa or 200 ya us se kam bill h to
    bill= (units - 100) * 5                   # yah pe 100 se jyda unit hua h (lekin us me se 100 unit ka fee 0 hoga baki jo bachega us me * 5 lgega)
elif units <= 300:
    bill= (100 * 5) + (units - 200) * 8 
else:
    bill= (100 * 5) + (100 * 8) + (units - 300) * 12
print("Total Electricity Bill: ₹", bill)
    
    