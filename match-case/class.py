# ########################################################################################

# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# operation = int(input("Enter operation :: \n 1) for addition : \n 2) for substraction : \n 3) for multiplication : \n 4) for division : \n Enter your choice:: "))

# match operation :
#     case 1 :
#         print("Addition is :", num1 + num2 )
#     case 2 :
#             print("Substraction is :" , num1 - num2 )
#     case 3 :
#                 print("Multiplication is :" , num1 * num2 )
#     case 4 :
#             print("Division is : " , num1 / num2 )
#     case _ :
#             print("Invalid oprator !!")



# ######################################################################################################

# num = int(input("Enter a number : "))
# choice = int(input("""Enter choices :
#                     1. Even
#                     2. Odd 
#                     3. Prime 
#                                 :: """))
# match choice :
#     case 1 :
#         if num % 2 == 0 :
#             print(num , "is Even .")
#         else :
#             print(num , "not Even .")
#     case 2 :
#         if num % 2 == 1 :
#             print(num , "is Odd .")
#         else :
#             print(num , "not Odd .")
#     case 3 :
#         count = 0

#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1

#         if count == 2:
#             print(num, "is Prime.")
#         else:
#             print(num, "not Prime.")
#     case _ :
#         print("Invalid choise !!")


# ######################################################################################################

# day = int(input("Enter a day :"))
# match day :
#     case 1 | 2 | 3| 4 | 5 :
#         print("Weekday")
#     case 6 | 7 :
#         print("Weekend")
#     case _ :
#         print("Invalid Day !!")
         
# ######################################################################################################

# marks = int(input("Enter marks : "))

# match marks:
#     case x if x >= 90:
#         print("A")
#     case x if x >= 75:
#         print("B")
#     case x if x >= 60:
#         print("C")
#     case x if x >= 40:
#         print("D")
#     case _:
#         print("Fail")

# ######################################################################################################


# balance = 2000000
# choice = int(input("""Enter your choice : 
#                         1 → Check Balance
#                         2 → Deposit Money
#                         3 → Withdraw Money
#                         4 → Exit
#                             ::  """))
# match choice :
#     case 1 :
#         print(f"Total balance is : {balance}")
#     case 2 :
#         deposite = int(input("Enter deposite amount : "))
#         print(f"Total balance is : {balance + deposite}")
#         balance += deposite
#     case 3 :
#         withdrawl = int(input("Enter withdrawl money : "))
#         if withdrawl > balance :
#             print("Insufficient amount ")
#         else :
#             print(f"Remaining amount : {balance - withdrawl}")
#     case 4 :
#         print("exit the banking menu ")
#     case _ :
#         print("Invalid choice")

######################################################################################################

balance = 2000000
choice = int(input("""Enter your choice : 
                        1 → Check Balance
                        2 → Deposit Money
                        3 → Withdraw Money
                        4 → Exit
                            ::  """))
match choice :
    case 1 :
        choice1 = int(input("""Enter choice : 
                                1 → Show  Balance
                                2 → Return to main menu """))
        match choice1 :
            case 1 :
                print(f"Total balance is : {balance}")
            case 2 : 
                print("Return to main menu")
            case _:
                print("Invalid choice!")

    case 2 :
        deposite = int(input("Enter deposite amount : "))
        match deposite :
            case x if deposite > 0  : 
                balance += deposite
                print("Amount deposited succefully ")
                print(f"New balance is : {balance}")
            case x :
                print("Invalid deposit amount!")
    case 3 :
        withdrawl = int(input("Enter withdrawl amount : "))
        match withdrawl :
            case x if withdrawl <= balance : 
                balance -= withdrawl
                print("Amount withdrawl succefully ")
                print(f"New balance is : {balance}")
            case x  :
                print("Invalid withdrawl amount!")
                        
    case 4 :
        print("exit the banking menu ")
    case _ :
        print("Invalid choice")


