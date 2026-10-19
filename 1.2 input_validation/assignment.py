# ###------------------------------------------------------------------------------------------------------------##

# # # question = 1

# while True :
#     marks = int(input("Enter your marks : "))
#     if 0 <= marks <= 100 :
#         print(f"marks = {marks}")
#         break

# # # question = 2 

# while True :
#     num = int(input("Enter a number : "))
#     if num > 0 :
#         print(f"You entered : {num}")
#         break

# # # question = 3 

# while True :
#     age = int(input("Enter age : "))
#     if 0 < age <= 120 :
#         print(f"You entered : {age}")
#         break
#     else :
#         print("ERROR!! Enter Correct input ")

# # # question = 4 

# while True :
#     choice = int(input("""Enter menu choice : 
#                                 1. View profile
#                                 2. Edit profile
#                                 3. Settings
#                                 4. Exit : """))
#     if 1 <= choice <= 4 :
#         match choice :
#             case 1 :
#                 print("Opening profile .") 
#             case 2 :
#                 print("Edit profile .") 
#             case 3 :
#                 print("Setting.") 
#             case 4 :
#                 print("Exit.") 
#         break
#     else :
#         print("Enter a valid choice : ")
    
# # # question = 5 

# password = input("Enter Password : ").strip()
# while len(password)<=8:
#     print("Enter a valid Password !!")
#     password = input("Enter Password : ").strip()
# print("Success")
    

# # # question = 6 

# temp = int(input("Enter temprature betweem -20 and 40  : "))
# while temp < -20 or temp > 40 :
#     print("Enter valid temprature : ")
#     temp = int(input("Enter temprature betweem -20 and 40  : "))
# print("Entered temprature ",temp)

# # # question = 7 

# bank_balance = 5000 
# withdrawl_amount = int(input("Enter withdrawl amount : "))
# while withdrawl_amount <= 0 or withdrawl_amount > 5000 :
#     print("Enter valid Amount : ")
#     withdrawl_amount = int(input("Enter withdrawl amount : "))
# print(f"Updated balance : {bank_balance-withdrawl_amount}")

# # # question = 8 

# username = input("Enter username : ").strip()
# while len(username) <= 5 or username == " " or " " in username :
#     print("Enter valid name!! ")
#     username = input("Enter username : ").strip()
# print(f"Accepted username {username}")

# # # question = 9 

# num = int(input("Enter a number that is divisible by 3 as well as 5 : "))
# while num % 3 != 0 and num % 5 != 0 or num < 0 :
#     print("Enter a valid number !!")
#     num = int(input("Enter a number that is divisible by 3 as well as 5 : "))
# print(f"You entered number = {num}")

# # # question = 10 

# secret_pin = 2468 
# count = 0 
# entered_pin = int(input("Enter pin : "))
# while secret_pin != entered_pin  :
#     count += 1 
#     print("Enter a valid Pin !!")
#     if count == 3 :
#         break
#     entered_pin = int(input("Enter pin : "))
# if entered_pin == secret_pin :
#     print("Successfully entered .")
# else :
#     print("Three attemptes done try after some time !! ")

# # # question = 11 

# num = int(input("Enter a  number between 10 and 50 : "))

# while num < 10 or num > 50 :
#     print("Enter a valid number !!")
#     num = int(input("Enter a  number between 10 and 50 : "))
# if num % 2 == 0 :
#     print(f"Even :: You entered {num}")
# else :
#     print(f"Odd :: You entered {num}")

# # # question = 12 

# balance = 2000 
# amount = int(input("Entere deposite amount : "))
# while amount <= 0  :
#     print("Enter valid amount !!")
#     amount = int(input("Entere deposite amount : "))
# print(f"""Deposit successfully 
#                 Current Balance  is : { balance + amount }""")

# # # question = 13 

# num = int(input("Enter a number between 1 and 100 : "))
# while num < 1 or num > 100 :
#     print("Enter a valid number !!")
#     num = int(input("Enter a number between 1 and 100 : "))
# print(f"You entered : {num}")

# # # question = 14 

# while True : 
#     marks = int(input("Enter marks : "))
#     if 0 <= marks <= 100 :
#         if marks <= 100 and marks >= 75:
#             print("Disstinction ")
#         elif marks < 75 :
#             print("First Class")
#         elif marks <= 60 :
#             print("Pass")
#         elif marks < 35 :
#             print("Fail")
#         break
#     else :
#         print(f"You entered : {marks}")

# # # question = 15 

# count = 0 
# while True :
#     while True :
#         username = input("Enter username atleast 5 character : ").strip()
#         if len(username) >= 5 :
#             break
#     while True :
#         password = (input("Enter password : ").strip())
#         for i in password :
#             if i == "" :
#                 count = count
#             count = count + 1 
#         if count >= 8 :
#             break
#     break 
# print(f"Username = {username} and Password is {password}")
    
# # question = 16 


