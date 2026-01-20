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


# # ================================Q2. Electricity Bill Generator============================================
# """Q2. Electricity Bill Generator

# Input:
# units

# Rules:
# ≤ 100 → ₹0
# 101–200 → ₹5/unit
# 201–300 → ₹8/unit
# 300 → ₹12/unit"""

# # Solution:
# units = int(input("Enter number of units consumed: "))

# if units <= 100:
#     bill= 0
    
#     """Logic:
#     First 100 units → Free
#     Bache hue units = units - 100
#     Har unit ka rate = ₹5"""
    
# elif units <= 200:                             #yaha pe 100 se jysa or 200 ya us se kam bill h to
#     bill= (units - 100) * 5                   # yah pe 100 se jyda unit hua h (lekin us me se 100 unit ka fee 0 hoga baki jo bachega us me * 5 lgega)
# elif units <= 300:
#     bill= (100 * 5) + (units - 200) * 8 
# else:
#     bill= (100 * 5) + (100 * 8) + (units - 300) * 12
# print("Total Electricity Bill: ₹", bill)
    
    

# # =================================================
# """Q3. Company Salary Hike System

# Input:
# salary
# rating

# Rules:
# Rating 5 → 30% hike
# Rating 4 → 20%
# Rating 3 → 10%
# Else → No hike"""

# # Solution:
# salary = float(input("Enter current salary: "))
# rating = int(input("Enter performance rating (1-5): ")) 
# if rating == 5:
#     hike = salary * 0.30
# elif rating == 4:
#     hike = salary * 0.20
# elif rating == 3:
#     hike = salary * 0.10
# else:
#     hike = 0

# print("Salary after hike: ₹", salary + hike)




# # =================================================
# """Q4. Ticket Pricing System

# Input:
# age
# gender
# time (morning/evening)

# Rules:
# Age < 12 → Free
# Female → 50% discount
# Morning show → 20% discount
# Base ticket price = 200"""

# # Solution:
# age = int(input("Enter age: "))
# gender = input("Enter gender (male/female): ")
# time = (input("Enter the show time (morning/evening): "))

# price = 200

# if age < 12 :
#     ticket_price = 0
    
# elif gender == "female":
#     ticket_price = price * 0.50
    
# elif time == "morning":
#     ticket_price = price * 0.80
    
# else:
#     ticket_price = price
# print("Ticket Price: ₹", ticket_price)
    
    
# # # =================================================
# """Q5. Bank Transaction Validator

# Input:
# balance
# amount

# Rules:
# Amount ≤ 0 → Invalid
# Amount > balance → Insufficient Balance
# Else → Transaction Success"""

# # Solution:
# balance = float(input("Enter current balance: "))
# amount = float(input("Enter transaction amount: "))
# if amount <= 0 :
#     print("Invalid Amount")
# elif amount > balance:
#     print("Insufficient Balance")
# else:
#     print("Transaction Success")
    

# # =================================================
# """Q6. Online Exam Result Engine

# Input:
# score

# Rules:
# ≥ 90 → Excellent
# ≥ 75 → Very Good
# ≥ 50 → Pass
# Else → Fail"""

# # Solution:
# score = float(input("Enter exam score: "))
# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Very Good")
# elif score >= 50:
#     print("Pass")   
# else:
#     print("Fail")
    

# # =================================================
# """Q7. Ride Fare Calculator

# Input:
# distance (km)

# Rules:
# First 5 km → ₹10/km
# Next 10 km → ₹8/km
# Remaining → ₹5/km"""

# # Solution:
# distance = float(input("Enter distance traveled (in km): "))
# if distance <= 5:
#     fare = distance * 10
# elif distance <= 10:
#     fare = (5 * 10) + (distance - 5) * 8    
# else:
#     fare = (5 * 10) + (10 * 8) + (distance - 10) * 5
# print("Total Ride Fare: ₹", fare)


# # =================================================
# """Q8. System Resource Check

# Input:
# RAM (GB)

# Rules:
# ≥ 16 → High Performance
# ≥ 8 → Medium
# ≥ 4 → Low
# Else → Not Supported"""

# # Solution:
# ram = float(input("Enter system RAM (in GB): "))
# if ram >= 16:
#     print("High Performance")
# elif ram >= 8:
#     print("Medium")
# elif ram >= 4:  
#     print("Low")  
# else:
#     print("Not Supported")  


# #===================================================================
# """
# Q10. Final Boss Question

# Input:
# income

# Rules:
# ≤ 2.5L → No Tax
# ≤ 5L → 5%
# ≤ 10L → 20%
# 10L → 30%"""

# # Solution:
# income = float(input("Enter annual income (in Lakh): "))
# if income <= 2.5:
#     tax = 0
# elif income <= 5:
#     tax = income * 0.05
# elif income <= 10:
#     tax = income * 0.20
# else:
#     tax = income * 0.30
# print("Total Tax: ₹", tax)


# #===================================================================
# """Q3. Advanced Number Analyzer

# Input:
# number

# Output:
# "Perfect Number"
# "Armstrong Number"
# "Palindrome Number"
# "Normal Number"""

# # Solution:
# number = int(input("Enter a number: "))
# # Check for Perfect Number
# sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
# if sum_of_divisors == number:
#     print("Perfect Number")
# # Check for Armstrong Number
# elif number == sum(int(digit) ** len(str(number)) for digit in str(number)):
#     print("Armstrong Number")
# # Check for Palindrome Number   
# elif str(number) == str(number)[::-1]:
#     print("Palindrome Number")
# else:
#     print("Normal Number")
    
# num = int(input("Enter the number:"))
# original_num = num
# print("Original Number:", original_num)

# sum_of_powers = 0   
# num_digits = len(str(num))     
# while num > 0:
#     digit = num % 10                          # % 10 se last digit nikalte hain
#     sum_of_powers += digit ** num_digits      # us digit ki power (len k barabar) nikal k sum m add kar diya
#     num = num // 10                           # last digit ko hatane k liye //10 kar diya
    
# # #Palindrome check
# # rev = 0
# # temp = original_num 
# # while temp > 0:
# #     digit = temp % 10
# #     rev = rev * 10 + digit
# #     temp = temp // 10

# rev = int(str(original_num)[::-1])  # ye ek line m palindrome check karne ka shortcut hai
    
# if sum_of_powers == original_num:
#     print(f"{original_num} is an Armstrong number.")  
      
# elif rev == original_num:
#     print(f"{original_num} is also a palindrome.")   
    
# else:
#     print(f"{original_num} is a Normal number.")


# #===================================================
# """Q11. Online Shopping Discount Engine

# Input:
# total_amount
# membership (yes/no)
# festival_sale (yes/no)

# Rules:
# Base discount:
# ≥ 5000 → 10%
# ≥ 10000 → 20%
# Membership → +5%
# Festival sale → +5%
# Max discount cap → 30%"""

# # Solution:
# total_amount = float(input("Enter total amount: "))
# membership = input("Are you a member? (yes/no): ").lower()
# festival_sale = input("Is it a festival sale? (yes/no): ")

# discount = 0

# if total_amount >= 5000:
#     discount += 10
#     if total_amount >= 10000:
#         discount += 20
#     else:
#         discount += 10   
         
# if membership == "yes":
#     discount += 5
    
# if festival_sale == "yes":
#     discount += 5
    
# if discount > 30:
#     discount = 30
  
#     print("Payable Amount:", total_amount - (total_amount * discount / 100))
# else:
#     print("No Discount Applicable")
    

# # =================================================
# """Q12. Company Promotion Eligibility System

# Input:
# experience (years)
# performance_rating (1–5)
# attendance (%)

# Rules:
# Experience ≥ 3
# Attendance ≥ 75
# Rating:
#     5 → Immediate Promotion
#     4 → Promotion
#     3 → On Hold
#     <3 → Not Eligible"""
    
# # Solution:
# experience = float(input("Enter years of experience: "))
# performance_rating = int(input("Enter performance rating (1-5): "))
# attendance = float(input("Enter attendance percentage: "))

# if experience >= 3 :
#     if attendance >= 75:
#         if performance_rating == 5:
#             print("Immediate Promotion")
#         elif performance_rating == 4:
#             print("Promotion")
#         elif performance_rating == 3:
#             print("On Hold")
#         else:
#             print("Not Eligible")
#     else:
#         print("Not Eligible due to low attendance")
        

# #===================================================
# """Q13. Traffic Signal & Speed Control System 
# Input:
# signal (red/yellow/green)
# speed

# Rules:
# Red:
# Speed > 0 → Fine 1000

# Yellow:
# Speed > 40 → Warning

# Green:
# Speed > 80 → Speed Fine 2000
# Else → Safe Driving"""

# # Solution:
# signal = input("Enter traffic signal color (red/yellow/green): ").lower()
# speed = float(input("Enter vehicle speed (in km/h): "))
# if signal == "red":
#     if speed > 0:
#         print("Fine: ₹1000")
#     else:
#         print("Safe Driving")
        
# elif signal == "yellow":
#     if speed > 40:
#         print("Warning: Slow Down")
#     else:
#         print("Safe Driving")
        
# elif signal == "green":
#     if speed > 80:
#         print("Speed Fine: ₹2000")
#     else:
#         print("Safe Driving")
        
# else:
#     print("Invalid Signal Color")
    
    
    
# # =================================================
# """Q14. Bank Loan Approval System
# Input:
# salary
# credit_score
# existing_loan (yes/no)

# Rules:
# Salary ≥ 25000
# Credit Score ≥ 700
# Existing Loan:
#     yes → Rejected
#     no → Approved"""
    
# # Solution:
# salary = float(input("Enter monthly salary: ")) 
# score = int(input("Enter credit score: "))
# loan = input("Do you have an existing loan? (yes/no): ")
# if salary >= 25000:
#     if score >= 700:
#         if loan == "no":
#             print("Loan Approved")
#         else:
#             print("Rejected: Existing Loan")
#     else:
#         print("Low Credit Score")
# else:
#     print("Low Salary")


# =================================================
"""Q15. Smart ATM Withdrawal System
User se:
account_balance
withdrawal_amount
account_type ("saving" / "current")

Rules:
Minimum balance:
    Saving → 1000
    Current → 5000
Withdrawal tab allow hoga jab:
    Amount > 0
    Amount balance se kam ho
    Withdrawal ke baad minimum balance bacha rahe

Output:
"Transaction Successful"
"Insufficient Balance"
"Minimum Balance Violation"
"Invalid Amount"""

# Solution:
amount_balance = float(input("Enter account balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))   
account_type = input("Enter account type (saving/current): ")

if account_type == "saving":
    min_balance = 1000
else:
    min_balance = 5000
    
if withdrawal_amount <= 0:
    print("Invalid Amount")
elif withdrawal_amount > amount_balance:
    print("Insufficient Balance")
elif (amount_balance - withdrawal_amount) < min_balance:
    print("Minimum Balance Violation")
else:
    print("Transaction Successful")
    
