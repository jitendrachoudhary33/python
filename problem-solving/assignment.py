######################### LEVEL 1 ####################################

# # Question = 1
# num = int(input("Enter a number:"))
# if num > 0:
#     print("Positive")
# elif num == 0 :
#     print("Zero")
# else :
#     print("Negative")

# # Question = 2
# num = int(input("Enter a number:"))
# if num > 0 and num % 2 == 0 :
#     print("Positive Even")
# elif num > 0 and num % 2 == 1 :
#     print("Positive Odd")
# elif num < 0 and num % 2 == 0 :
#     print("Negative Even")
# elif num < 0 and num % 2 == 1 :
#     print("Negative Odd")
# else :
#     print("Zero")

# # Question = 3
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# if a > b :
#     print(f"{a} is greater than {b}")
# elif a < b :
#     print(f"{b} is greater than {a}")
# else :
#     print("Both are equal")

# # Question = 4
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))
# if a == b == c :
#     print("All are equal")
# elif a >= b >= c :
#     print(f"Smallest is {c}")
# elif a >= b <= c :
#     print(f"Smallest is {b}")
# elif a <= b <= c :
#     print(f"Smallest is {a}")


    

# # Question = 5 
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))
# if a == b == c :
#     print("All are equal")
# elif a >= b >= c :
#     print(f"Largest is {a}")
# elif a <= b >= c :
#     print(f"Largest is {b}")
# elif a <= b <= c :
#     print(f"Largest is {c}")

# # Question = 6
# num = int(input("Enter a number :"))
# if num % 5 == 0 and num % 11 == 0 :
#     print(f"{num} is divisible by both 5 and 11")
# elif num % 5 == 0 :
#     print(f"{num} is divisible by 5")
# elif num % 11 == 0 :
#     print(f"{num} is divisible by 11")
# else :
#     print("divisible by neither")

# # Question = 7
# num = int(input("Enter a number :"))
# if num % 3 == 0 or num % 7 == 0 :
#     print(f"{num} is divisible by either 3 or 7")
# elif num % 3 == 0 :
#     print(f"{num} is divisible by 3")
# elif num % 7 == 0 :
#     print(f"{num} is divisible by 7")
# else :
#     print("divisible by neither")

# # Question = 8
# marks = int(input("enter your marks:"))
# if marks >= 40 and marks < 100 :
#     print("Pass!!")
# elif marks < 40 and marks > 0 :
#     print("Fail!!")
# else :
#     print("Invalid marks")


# # Question  = 9
# marks = int(input("Enter your marks:"))
# if marks >= 90 and marks <= 100 :
#     print("Grade A")
# elif marks >= 80 and marks <=89 :
#     print("Grade B")
# elif marks >= 70 and marks <= 79 :
#     print("Grade C")
# elif marks >= 60 and marks <= 69 :
#     print("Grade D")
# elif marks >= 40 and marks <= 59 :
#     print("Grade E")
# elif marks >=0 and marks < 40 :
#     print("Fail!!")
# else :
#     print("Enter valid marks")

# # Question = 10 
# age = int(input("Enter your age:"))
# if age >= 18 :
#     print("Can Vote ")
# elif age < 18 and age > 0 :
#     print("Cannot Vote")
# else :
#     print("Invalid age")

###################### LEVEL 2 ###########################

# # Question = 11 
# year = int(input("Enter a year :"))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("Leap Year")
# else :
#     print("Not a leap year")

# # Queestion = 12                ######################## DOUBT ########################################
# character = int(input("Enter any one character:"))
# if character >= 0 and character <= 0 :
#     print("Digit")
# elif character >= 97 and character <= 133 :
#     print("Lowercase alphabet")

# elif character >=65 and character <= 91 :
#     print("Uppercase alphabet")

# elif character == "@" :
#     print("Special characters")

# # Question = 13
# ch = input("Enter a character :")
# if ch.lower() in "aeiou":
#     print("Vowel")
# elif ch.lower() in "bcdefghijklmnopqrstuvwxyz" :
#     print("Consonant")
# else :
#     print("Invalid input")

# # Question = 14
# cost_price = int(input("Cost price:"))
# selling_price = int(input("Selling price:"))
# if cost_price > selling_price :
#     print(f"loss = {cost_price - selling_price}")
# elif selling_price > cost_price :
#     print(f"profit = { selling_price - cost_price}")
# else :
#     print("Invalid data")

# # Question = 15
# cost_price = int(input("Cost price:"))
# selling_price = int(input("Selling price:"))
# if cost_price < 0 or selling_price < 0 :
#     print("Invalid data")
# elif cost_price > selling_price :
#     print(f"loss = {int(cost_price - selling_price) / cost_price * 100} %")
# elif selling_price > cost_price :
#     print(f"profit = {(selling_price - cost_price) / cost_price * 100} %")

# # Question = 16 
# unit = int(input("Enter your unit :"))
# if unit > 0 and unit <= 100 :
#     print(f"Bill is = {unit * 5 }")
# elif unit > 100 and unit <= 200 :
#     print(f"Bill is = {(unit - 100) * 7 + 100 * 5}")
# elif unit > 200  :
#     print(f"Bill is = {(unit - 200) * 10 + 100 * 7 + 100 * 5}")

# Question = 17 
# oprater = int(input("1.Addition:\n2.Substraction:\n3.Mulitplication:\n4.Division:\nEnter operater ::"))
# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))

# a = int(input(Enter first no.-  ))
# b = int(input(Enter second no.-  ))
a = int(input("Enter a first number"))
op = input("Enter opt(+,-,*,/)")
b = int(input("enter second num"))
if op == "+" :
    print("Answer:",a+b)
elif op == "-":
    print("Answer:",a-b)
elif op == "*":
    print("Answer:",a*b)










# # Question = 19
# a = int(input("Enter  a number :"))
# if a < 0 :
#     print("Negative")
# elif a >= 0 and a <= 10 :
#     print("Number is between 0 and 10")
# elif a >= 11 and a <= 50 :
#     print("Number is between 11 and 50")
# elif a >= 51 and a <= 100 :
#     print("Number is between 51 and 100")
# else :
#     print("Above 100")

# Question = 20

