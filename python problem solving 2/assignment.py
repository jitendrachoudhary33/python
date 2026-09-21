# # Question = 1
# # IPO 
# Input: Two numbers
# Process: Add the two numbers
# Output: Sum

# #Algorithm
# Start
# Input two numbers a and b
# Calculate sum = a + b
# Print the sum
# Stop
# Dry Run

# Test  1 ;
# a = 10, b = 20
# sum = 10 + 20 = 30
# Output: 30

# Test  2 ;
# a = 5, b = 7
# sum = 5 + 7 = 12
# Output: 12
 
## Code
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum:", sum)



# # Question = 2

# #IPO 
# Input: One number
# Process: Check if the number is divisible by 2
# Output: Even or Odd

# #Algorithm
# Start
# Input a number
# Check number % 2
# If the remainder is 0, print Even
# Otherwise, print Odd
# Stop
# Dry Run

# Test  1:
# number = 10
# 10 % 2 = 0
# Output: Even

# Test  2:
# number = 7
# 7 % 2 = 1
# Output: Odd

## Code 
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# # Question = 3
# IPO 
# Input: Three numbers
# Process: Compare the three numbers
# Output: Largest number

# Algorithm
# Start
# Input three numbers a, b, and c
# Compare the three numbers
# Find the largest number
# Print the largest number
# Stop

# Dry Run

# Test  1:
# a = 10, b = 25, c = 15
# Largest = 25
# Output: 25

# Test  2:
# a = 50, b = 20, c = 40
# Largest = 50
# Output: 50

##Code 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest number:", largest)

# # Question = 4
# IPO 
# Input: Person's age
# Process: Check if age is 18 or more
# Output: Eligible or Not Eligible

# Algorithm
# Start
# Input the person's age
# Check if age >= 18
# If true, print Eligible to vote
# Otherwise, print Not eligible to vote
# Stop
# Dry Run

# Test  1:
# age = 20
# 20 >= 18 → True
# Output: Eligible to vote

# Test  2:
# age = 16
# 16 >= 18 → False
# Output: Not eligible to vote

## Code
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")




# # Question = 5
# #IPO 
# Input: Price of an item
# Process: Give 20% discount if price is ₹2000 or more
# Output: Final price

# #Algorithm
# Start
# Input the price
# Check if price >= 2000
# If true, calculate 20% discount
# Subtract discount from the original price
# Otherwise, keep the original price
# Print the final price
# Stop

# #Dry Run

# Test  1:
# price = 2500
# Discount = 2500 × 20 / 100 = 500
# Final price = 2500 - 500 = 2000
# Output: 2000

# Test  2:
# price = 1500
# 1500 < 2000 → No discount
# Final price = 1500
# Output: 1500

##Code 
price = float(input("Enter item price: "))
if price >= 2000:
    discount = price * 20 / 100
    final_price = price - discount
else:
    final_price = price
print("Final price:", final_price)



# # Question = 6
#  #IPO 
# Input: Marks of three subjects
# Process: Calculate average and check if average is at least 40
# Output: Average and Pass/Fail

# #Algorithm
# Start
# Input marks of three subjects
# Calculate average
# Check if average is >= 40
# If true, print Pass
# Otherwise, print Fail
# Stop

# #Dry Run
# Test  1:
# Marks = 50, 60, 70
# Average = (50 + 60 + 70) / 3
# Average = 180 / 3
# Average = 60
# 60 >= 40 → Pass
# Output:
# Average: 60
# Pass

# Test  2:
# Marks = 30, 35, 40
# Average = (30 + 35 + 40) / 3
# Average = 105 / 3
# Average = 35
# 35 < 40 → Fail
# Output:
# Average: 35
# Fail

## Code
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))
average = (mark1 + mark2 + mark3) / 3
print("Average:", average)
if average >= 40:
    print("Pass")
else:
    print("Fail")