# ##------------------------------------------------------------------------------------------------------------------##

# # question = 1 

# choice = int(input("""Enter your choice : 
#                         1 → Pizza
#                         2 → Burger
#                         3 → Pasta
#                         4 → Sandwich 
#                                 ::   """))
# match choice :
#     case 1 :
#         print("You selected Pizza.")
#     case 2 :
#         print("You selected Burger.")
#     case 3 :
#         print("You selected Pasta.")
#     case 4 :
#         print("You selected Sandwich.")
#     case _ :
#         print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 2 

# choice = int(input("""Enter your choice : 
#                         1 → Wi-Fi
#                         2 → Bluetooth
#                         3 → Mobile Data
#                         4 → Airplane Mode
#                         5 → Exit
#                                 ::  """))
# match choice :
#     case 1 :
#         print("Wi-Fi Selected.")
#     case 2 :
#         print("Bluetooth Selected.")
#     case 3 :
#         print("Mobile Data Selected.")
#     case 4 :
#         print("Airplane Mode.")
#     case 5 :
#             print("Exit.")
#     case _ :
#         print("Invalid Setting ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 3 
# choice = int(input("""Enter your choice : 
#                         1 → Check Balance
#                         2 → Withdraw Money
#                         3 → Deposit Money
#                         4 → Change PIN
#                         5 → Exit
#                                 ::  """))
# match choice :
#     case 1 :
#         print("Check balance.")
#     case 2 :
#         print("Withdrawl Money.")
#     case 3 :
#         print("Deposite Money.")
#     case 4 :
#         print("Change PIN.")
#     case 5 :
#             print("Exit.")
#     case _ :
#         print("Invalid Choice. ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 4 

# color = input("Enter signal. : ").lower()

# match color :
#     case "red" :
#         print("Stop")
#     case "yellow" :
#         print("Wait")
#     case "green" :
#         print("Go")
#     case _ :
#         print("Invalid color !! ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 5
 
# choice = int(input("""Enter your choice : 
#                         1 → View profile
#                         2 → View Courses
#                         3 → View Marks
#                         4 → View Attendence
#                         5 → Logout
#                                 ::  """))
# match choice :
#     case 1 :
#         print("Opening Profile.")
#     case 2 :
#         print("Opening courses.")
#     case 3 :
#         print("Opening Marks.")
#     case 4 :
#         print("Opening Attendence.")
#     case 5 :
#             print("Logout.")
#     case _ :
#         print("Invalid Choice. ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 6 

# choice = int(input("""Enter your choice : 
#                         1 → Electronics
#                         2 → Clothing
#                         3 → Books
#                         4 → Grocery
#                         5 → Exit
#                                 ::  """))
# match choice :
#     case 1 :
#         print("Opening Electronics.")
#     case 2 :
#         print("Opening courses.")
#     case 3 :
#         print("Opening Marks.")
#     case 4 :
#         print("Opening Attendence.")
#     case 5 :
#             print("Logout.")
#     case _ :
#         print("Invalid Choice. ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 7 

# choice = int(input("""Enter your choice : 
#                         1 → Account Balance
#                         2 → Mini Statement
#                         3 → Fund Transfer
#                         4 → Bill Payment
#                         5 → Customer Support
#                                 ::  """))
# match choice :
#     case 1 :
#         print("Opening Account Balance.")
#     case 2 :
#         print("Opening Mini Statement.")
#     case 3 :
#         print("Opening Fund Transfer.")
#     case 4 :
#         print("Opening Bill Payment.")
#     case 5 :
#         print("Customer Support.")
#     case _ :
#         print("Invalid Choice. ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 8 

# choice = int(input("""Enter your choice : 
#                         1 → Morning Show
#                         2 → Afternoon Show
#                         3 → Evening Show
#                         4 → Night Show
#                                 ::  """))
# match choice :
#     case 1 :
#         print("Morning Show Selected.")
#     case 2 :
#         print("Afternoon Show Selected.")
#     case 3 :
#         print("Evening Show Selected.")
#     case 4 :
#         print("Night Show Selected.")
#     case _ :
#         print("Invalid Choice. ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 9 

# weather = input("Enter weather : ").lower()    ## || sunny , rainy , cloudy , snowy || ##

# match weather :
#     case "sunny" :
#         print("Wear sunglasses")
#     case "rainy" :
#             print("Carry an umbrella")
#     case "cloudy" :
#             print("Weather may change")
#     case "snowy" :
#             print("Wear warm clothes")
#     case _ :
#             print("Unknown Weather.")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 10 

# payment = input("Enter Payment Mathod : ").lower()

# match payment :
#     case "upi" :
#         print(" UPI Payment Selected")
#     case "card" :
#             print("Card Payment Selected")
#     case "cash" :
#             print("Cash Payment Selected")
#     case "wallet" :
#             print("Wallet Payment Selected")
#     case _ :
#             print("Ivalid payment mathod.")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 11 

# type = input("Enter file extension : ")
# match type :
#     case "pdf" :
#         print("pdf file.")
#     case "jpg" :
#         print("jpg file.")
#     case "png" :
#         print("png file.")
#     case "mp3" :
#         print("Audio File.")
#     case "mp4" :
#             print("Video File.")
#     case _ :
#         print("Unknown File Type . ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 12

# role = input("""Enter Role from → admin , teacher , student , guest  
#                         :: """).lower()

# match role :
#     case "admin":
#         print(" Full Access")
#     case "teacher":
#         print(" Teacher Dashboard")
#     case "student":
#         print(" Student Dashboard")
#     case "guest" :
#         print("Limited Access")
#     case _ :
#         print("Invalid Role !!")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 13 


# day = int(input("""Enter day number : 
#                         1 → Monday
#                         2 → Tuesday
#                         3 → Wednesday
#                         4 → Thursday
#                         5 → Friday
#                         6 → Saturday
#                         7 → Sunday
#                                 ::  """))
# match day :
#     case 1 | 2 | 3 | 4 | 5 :
#         print("Weekday.")
#     case 6 | 7 :
#         print("Weekend.")
#     case _ :
#         print("Invalid day number. ")

##------------------------------------------------------------------------------------------------------------------##

# question =  14 





