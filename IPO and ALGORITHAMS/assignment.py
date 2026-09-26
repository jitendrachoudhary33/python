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

# Test  1 ;
# a = 20, b = 30
# sum = 20 + 30 = 50
# Output: 50

# Test  2 ;
# a = 7, b = 7
# sum = 7 + 7 = 14
# Output: 14
 
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

# Test  1:
# number = 10
# 14 % 2 = 0
# Output: Even

# Test  2:
# number = 7
# 3 % 2 = 1
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


# Test  1:
# a = 20, b = 35, c = 25
# Largest = 35
# Output: 35

# Test  2:
# a = 90, b = 30, c = 10
# Largest = 90
# Output: 90

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

# Test  1:
# age = 30
# 30 >= 18 → True
# Output: Eligible to vote

# Test  2:
# age = 16
# 13 >= 18 → False
# Output: Not eligible to vote

## Code
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not eligible ")




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



# Test  1:
# price = 5700
# Discount = 5700 × 0.2 = 1140
# Final price = 5700 - 1140 = 4560
# Output: 4560

# Test  2:
# price = 1500
# 1500 < 2000 → No discount
# Final price = 1500
# Output: 1500

##Code 
price = float(input("Enter item price: "))
if price >= 2000:
    discount = price * 0.20
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
    print("Pass!!")
else:
    print("Fail!!")