    # Task = 1
number = int(input("Enter any number:"))
if number > 10:
    print("Greater than 10 ")

    # Task = 2
age = int(input("Enter your age"))
if age >=18:
    print("Adult")

    # Task = 3
number = int(input("Enter any number:"))
if number > 0 :
    print("Positive")

    # Task = 4
marks = int (input("Enter your marks:"))
if marks >= 40 :
    print("PASS!!")

    # Task = 5
number = int(input("Enter any number:"))
if number == 0 :
    print("zero")

    # Task = 6
number = int(input("Enter any number:"))
if number > 0 :
    print("Positive")
else :
    print("Not Positive")

    # Task = 7
age = int(input("Enter your age :"))
if age >= 18 :
    print("Adult")
else :
    print("Not-Adult")

    # Task = 8
number = int(input("Enter a number :"))
if number % 2 == 0:
    print("Even")
else:
    print("odd")

    # Task = 9
marks = int(input("Enter your marks:"))
if marks >= 40:
    print("Pass")
else :
    print("fail")

    # Task = 10
a = int(input("Enter first number:"))
b = int(input("Enter seccond number:"))
if a > b :
    print(f"{a} is greater ")
else :
    print(f"{b} is grater")
    
    # Task = 11
marks = int(input("Enter your marks:"))
if marks >= 90 :
    print("A")
elif marks >= 75 :
    print("B")
elif marks >= 60 :
    print("C")
elif marks > 40 :
    print("D")
else:
    print("F")

    # Task = 12
number = int(input("Enter any number :"))
if number > 0 :
    print("Positive")
elif number == 0 :
    print("Zero")
else :
    print("negetive")
 
    # Task = 13
number = int(input("Enter a number :"))
if number == 1 :
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
else :
    print("other")

    # Task = 14
students_marks = int(input("Enter your marks:"))
if students_marks >= 90 :
    print("Excellent")
elif students_marks >= 75 :
    print("Good")
elif students_marks >= 35 :
    print("Pass")
else :
    print("Fail")

    # Task =15
number = int(input("Enter a number:"))
if number == 1 :
    print(1)
elif number == 2 :
    print(2)
elif number == 3 :
    print(3)
else :
    print("other")

    # Task = 16
age = int(input("Enter your age :"))
if age >= 18 :
    if age <= 60 :
        print("Between 18 and 60")
else :
    print("other")

    # Task = 17 
marks = int(input("Enter your marks :"))
if marks >= 40 :
    if marks >= 75 :
        print("Good")
    else :
        print("passed")
else :
    print("Failed")

    # Task = 18
number = int(input("Ente a number :"))
if number > 0 :
    print("positive")
    if number > 100 :
        print("greater than 100")
else :
    print("negative")

    # Task = 19
age = int(input("Enter your age:"))
if age >= 18 :
    if age >= 60 :
        print("Don't able for vote")
    else :
        print("Able to vote")

    # Task = 20
number = int(input("Enter a number:"))
if number != 0 :
    if number > 0 :
        print("Positive")
    else :
        print("Negative")
else : 
    print("Zero")

    # Task = 21
age = int(input("Enter your age:"))
marks = int(input("Enter your marks:"))
if age >= 18 and marks >= 40 :
    print("Eligible")
else :
    print("Not Eligible")

    # Task = 22
number = int(input("Enter a number:"))
if number < 10 or number > 100 :
    print("Special")
else :
    print("Random")

    # Task = 23                                                ##########################DOUBT#################
age = int(input("Enter your age :"))
has_id = input("has_id: True/False::")
if age >= 18 :  
    if has_id is True:
        print("Allowed")
    elif has_id is False:
        print("Not allowed")
    else:
        print("Put a valid data")
else :
    print("Not Allowed")

    # Task = 24
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
if a > 10 and b >10 :
    print("Both are greater than 10")
else :
    print("Invalid")

    # Task = 25
number = int(input("Enter a number:"))
if number < 0 or number > 100 :
    print("Either greater than 100 and less than 0")
else :
    print("Between 0 and 100")

    # Task = 26                               #################DOUBT############################
collage = input("collage :")
is_closed = False
if not is_closed :
    print("Open")

    # Task = 27
number = int(input("Enter a number :"))
if number >= 10 and number <= 50:
    print("Number in between 10 and 50")
else :
    print("Number not in between 10 and 50")

    # Task = 28
number = int(input("Enter a number :"))
if number < 10 or number > 50 :
    print("Not in between 10 and 50")
else :
    print(" In between 10 and 50")

    # Task = 29
is_student = input("is_student:").strip()
has_id = input("has_id:").strip()
has_ticket = input("has_ticket:").strip()
if is_student == "yes" :
    if has_id == "yes" :
        if has_ticket =="yes" : 
            print("Allowed")
        else :
            print("Not Allowed")
    else :
        print("Not Allowed")
else :
    print("Not allowed")
   
    # Task = 30
age = int(input("Enter your age :"))
marks = int(input("Enter your marks :"))
has_id = ("Has ID? True or False :").lower == True 
if age >= 18 and marks >= 40 and :
    print("Eligible")
else :
    print("Not Eligible")