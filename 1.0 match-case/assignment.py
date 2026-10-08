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

# ##------------------------------------------------------------------------------------------------------------------##

# # question =  14 

# priority = int(input("""Enter your priority :
#                             1 → Low
#                             2 → Medium
#                             3 → High
#                             4 → Critical  
#                                     ::   """))
# match priority :
#     case 1 | 2 :
#         print("Normal Priority")
#     case 3 | 4 :
#         print("Urgent Priority")
#     case _ :
#         print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 15 


# membership = int(input("""Enter your priority :
#                             1 → Bronze
#                             2 → Silver
#                             3 → Gold
#                             4 → Platinum
#                                     ::   """))
# match membership :
#     case 1 | 2 :
#         print("Basic Membership")
#     case 3 | 4 :
#         print("Premium Membership")
#     case _ :
#         print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 16

# select = int(input("""Enter your type : 
#                             1 → Student
#                             2 → Teacher        
#                                     :: """))
# match select :
#     case 1 :
#         choice = int (input("""Enter your choice :
#                                 1 → View Courses
#                                 2 → View Marks
#                                 3 → View Attendance  
#                                         ::   """))
#         match choice :
#             case 1 :
#                 print("Opening View Courses")
#             case 2 :
#                 print("Opening View Marks")
#             case 3 :
#                 print("Opening View Attendance  ") 
#             case _ :
#                 print("Invalid choice") 
#     case 2 :
#         choice = int (input("""Enter your choice :
#                                         1 → View Students
#                                         2 → Enter Marks
#                                         3 → View Attendance 
#                                                 ::   """))
#         match choice :
#             case 1 :
#                 print("Opening View Students")
#             case 2 :
#                 print("Opening Enter Marks")
#             case 3 :
#                 print("Opening View Attendance  ") 
#             case _ :
#                     print("Invalid choice")  
#     case _ :
#         print("Invalid choice")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 17 

# type = int(input("""Enter your account type :
#                             1 → Savings
#                             2 → Current
#                                     :: """))
# match type :
#     case 1 :
#         choice = int(input("""Enter your choice :
#         `                           1 → Check Balance
#                                     2 → Deposit
#                                     3 → Withdraw
#                                             :: """))
#         match choice :
#             case 1 :
#                 print("""Savings Account
#                          Check Balance Selected""")
#             case 2 :
#                 print("""Savings Account
#                          Deposit Selected""")
#             case 3 :
#                 print("""Savings Account
#                          Withdraw Selected""")
#             case _ :
#                 print("""Savings Account
#                          Invalid choice""")
#     case 2 :
#         choice = int(input("""Enter your choice :
#                 `                           1 → Check Balance
#                                             2 → Deposit
#                                             3 → Withdraw
#                                                     :: """))
#         match choice :
#             case 1 :
#                 print("""Current Account
#                          Check Balance Selected""")
#             case 2 :
#                 print("""Current Account
#                          Deposit Selected""")
#             case 3 :
#                 print("""Current Account
#                          Withdraw Selected""")
#             case _ :
#                 print("""Current Account 
#                          Invalid choice""")
#     case _ :
#         print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 18                                                                                                                                                                
  
# type = int(input("""Enter your category :
#                             1 → Electronics
#                             2 → Clothing
#                                     :: """))
# match type :
#     case 1 :
#         choice = int(input("""Enter your product :
#         `                           1 → Mobile
#                                     2 → Laptop
#                                     3 → Headphones
#                                             :: """))
#         match choice :
#             case 1 :
#                 print("""Mobile Selected""")
#             case 2 :
#                 print("""Laptop Selected""")
#             case 3 :
#                 print("""Headphones Selected""")
#             case _ :
#                 print("""Invalid choice""")
#     case 2 :
#         choice = int(input("""Enter your product  :
#                 `                           1 → Shirt
#                                             2 → Jeans
#                                             3 → Shoes
#                                                     :: """))
#         match choice :
#             case 1 :
#                 print("""Shirt Selected""")
#             case 2 :
#                 print("""Jeans Selected""")
#             case 3 :
#                 print("""Shoes Selected""")
#             case _ :
#                 print("""Invalid choice""")
#     case _ :
#         print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 19 

# type = int(input("""Enter your category :
#                             1 → Vegetarian
#                             2 → Non-Vegetarian
#                                     :: """))
# match type :
#     case 1 :
#         choice = int(input("""Enter your food  :
#         `                           1 → Paneer
#                                     2 → Dal
#                                     3 → Veg Biryani
#                                             :: """))
#         match choice :
#             case 1 :
#                 print("""Paneer Selected""")
#             case 2 :
#                 print("""Dal Selected""")
#             case 3 :
#                 print("""Veg Biryani Selected""")
#             case _ :
#                 print("""Invalid choice""")
#     case 2 :
#         choice = int(input("""Enter your food  :
#                 `                           1 → Chicken Biryani
#                                             2 → Chicken Curry
#                                             3 → Fish Fry
#                                                     :: """))
#         match choice :
#             case 1 :
#                 print("""Chicken Biryani Selected""")
#             case 2 :
#                 print("""Chicken Curry Selected""")
#             case 3 :
#                 print("""Fish Fry Selected""")
#             case _ :
#                 print("""Invalid choice""")
#     case _ :
#         print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 20 

# operator = int(input("""Select the type of operator : 
#                                  1 → Addition (+)
#                                  2 → Substract (-)
#                                  3 → Multiplication (*)
#                                  4 → Division (/)
#                                             ::  """))
# num1 = int(input("Enter first number :"))
# num2 = int(input("Enter second number :"))
# match operator :
#     case 1 :
#         print(f"Result = {num1 + num2}")
#     case 2 :
#             print(f"Result = {num1 - num2}")
#     case 3 :
#             print(f"Result = {num1 * num2}")
#     case 4 :
#             if num1 / 0 or num2 / 0 :
#                 print(f"Result = {"not define"}")
#             else :
#                 print(f"Result = {num1 / num2}")
#     case _ :
#             print(f"Invallid choice")
    
# ##------------------------------------------------------------------------------------------------------------------##

# # question = 21 

# choice = int(input("Enter choice: "))
# temperature = float(input("Enter temperature: "))

# match choice:
#     case 1:
#         fahrenheit = (temperature * 9 / 5) + 32
#         print("Temperature =", fahrenheit, "F")

#     case 2:
#         celsius = (temperature - 32) * 5 / 9
#         print("Temperature =", celsius, "C")

#     case _:
#         print("Invalid choice")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 22 

# choice = int(input("Enter choice: "))
# value = float(input("Enter value: "))

# match choice:
#     case 1:
#         result = value * 1000
#         print(result, "meters")

#     case 2:
#         result = value / 1000
#         print(result, "kilometers")

#     case 3:
#         result = value * 1000
#         print(result, "grams")

#     case 4:
#         result = value / 1000
#         print(result, "kilograms")

#     case _:
#         print("Invalid choice")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 23 

# account = int(input("""Enter account type: 
#                                 1 → Savings
#                                 2 → Current"""))

# match account:
#     case 1:
#         print("Savings Account")
#         amount = float(input("Enter amount: "))

#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case 2:
#         print("Current Account")
#         amount = float(input("Enter amount: "))

#         if amount > 0:
#             print("Withdrawal Request Accepted")
#         else:
#             print("Invalid Amount")

#     case _:
#         print("Invalid Account Type")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 24
 
# menu = int(input("""Enter choice : 
#                             1 → Start Exam
#                             2 → View Result
#                             3 → Exit
#                                     :: """))
# match menu :
#     case 1 :
#         age = int(input("Enter your age : "))
#         if age >= 18 :
#             print("You can start the exam")
#         else :
#             print("Age must be atleast 18 ")
#     case 2 :
#         print("viewing result")
#     case 3 :
#         print("Exit")
#     case _ :
#         print("Invalid choice ")
        
# ##------------------------------------------------------------------------------------------------------------------##

# # question = 25

# ticket = int(input("""Enter movie type : 
#                             1 → Regular
#                             2 → Premium
#                             3 → VIP
#                                 :: """))
# age = int(input("Enter your age : "))
# if age <= 5 :
#     print("Free Entry ")
# else :
#     match ticket :
#         case 1 :
#             print("Regular type Selected ")
#         case 2 :
#             print("Premium type Selected ")
#         case 3 :
#             print("ViP type selected ")
#         case _ :
#             print("Invalid choice")
        
# ##------------------------------------------------------------------------------------------------------------------##

# # question = 26

# controller = int(input("""Enter what you want to conntrol : 
#                                     1 → Light
#                                     2 → Fan
#                                     3 → AC
#                                     4 → TV
#                                         :: """)) 
# match controller :
#     case 1 :
#         print("AC Controller Opened")
#     case 2 :
#         print("AC Controller Opened")
#     case 3 :
#         print("AC Controller Opened")
#     case 4 :
#         print("AC Controller Opened")
#     case _ :
#         print("Invalid choice")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 21 

# menu = int(input("""Enter your choice :
#                                 1 → General Medicine
#                                 2 → Cardiology
#                                 3 → Orthopedics
#                                 4 → Pediatrics
#                                 5 → Emergency 
#                                         ::   """))
# match menu :
#     case 1 :
#         print("General Medicine Department")
#     case 2 :
#             print("Cardiology Department")
#     case 3 :
#             print(" Orthopedics Department")
#     case 4 :
#             print("Pediatrics Department")
#     case 5 :
#             print("Emergency Department")
#     case _ :
#             print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 28 

# menu = int(input("""Enter your choice :
#                                 1 → Book Ticket
#                                 2 → Cancel Ticket
#                                 3 → Check PNR
#                                 4 → Train Schedule
#                                 5 → Exit 
#                                         ::   """))
# match menu :
#     case 1 :
#         print("Booking Ticket")
#     case 2 :
#             print("Canceling Ticket")
#     case 3 :
#             print("Checking PNR")
#     case 4 :
#             print("Opening Train Schedule")
#     case 5 :
#             print("Exit")
#     case _ :
#             print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 29 

# menu = int(input("""Enter your choice :
#                                 1 → Search Book
#                                 2 → Issue Book
#                                 3 → Return Book
#                                 4 → View Issued Books
#                                 5 → Exit
#                                         ::   """))
# match menu :
#     case 1 :
#         print("Search Bookt")
#     case 2 :
#             print("Issue Book")
#     case 3 :
#             print("Return Book")
#     case 4 :
#             print("View Issued Books")
#     case 5 :
#             print("Exit")
#     case _ :
#             print("Invalid choice ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 30 

# menu = int(input("""Enter your choice :
#                                 1 → placed
#                                 2 → confirmed
#                                 3 → preparing
#                                 4 → out_for_delivery
#                                 5 → delivered
#                                 6 → cancelled
#                                         ::   """))
# match menu :
#     case 1 :
#         print("Your order is placeed")
#     case 2 :
#             print("Order conform")
#     case 3 :
#             print("Order preparing")
#     case 4 :
#             print("Order is on the way ")
#     case 5 :
#             print("order delivered")
#     case 6 :
#             print("Order cencelled ")
#     case _ :
#           print("Invalid choice")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 31 

banking_type = int(input("Enter banking type: "))

match banking_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Transfer Selected")
            case 3:
                print("Loan Selected")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Banking Type Selected")

##------------------------------------------------------------------------------------------------------------------##

# # question = 32

role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Marks")
            case 2:
                print("Opening Student Attendance")
            case 3:
                print("Opening Student Homework")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Enter Marks")
            case 2:
                print("Opening Teacher Attendance")
            case 3:
                print("Opening Assign Homework")
            case _:
                print("Invalid Option Selected")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Child Marks")
            case 2:
                print("Opening Child Attendance")
            case 3:
                print("Opening Contact Teacher")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Role Selected")  

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 33

transport = int(input("Enter transport type: "))

match transport:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Flight Economy Selected")
            case 2:
                print("Flight Business Selected")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Train Sleeper Selected")
            case 2:
                print("Train AC Selected")
            case _:
                print("Invalid Option Selected")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Bus Ordinary Selected")
            case 2:
                print("Bus Volvo Selected")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Transport Selected") 

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 34 

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Start Game Selected")
    case 2:
        print("Load Game Selected")
    case 3:
        setting_choice = int(input("Enter settings option: "))
        match setting_choice:
            case 1:
                print("Sound Settings Selected")
            case 2:
                print("Graphics Settings Selected")
            case 3:
                print("Controls Settings Selected")
            case _:
                print("Invalid Settings Choice")
    case 4:
        print("Exiting Game...")
    case _:
        print("Invalid Choice") 

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 35 

category = int(input("Enter category: "))

match category:
    case 1:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Item Selected")
    case 2:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Item Selected")
    case 3:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Item Selected")
    case 4:
        item = int(input("Enter item: "))
        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Item Selected")
    case _:
        print("Invalid Category Selected")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 36 

payment_type = int(input("Enter payment type: "))

match payment_type:
    case 1:
        upi_option = int(input("Enter option: "))
        match upi_option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid Option Selected")
    case 2:
        card_option = int(input("Enter option: "))
        match card_option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option Selected")
    case 3:
        wallet_option = int(input("Enter option: "))
        match wallet_option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Payment Type Selected")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 37

category = int(input("Enter category: "))

match category:
    case 1:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Course Selected")
    case 2:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Course Selected")
    case 3:
        course = int(input("Enter course: "))
        match course:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Course Selected")
    case _:
        print("Invalid Category Selected")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 38

option = int(input("Enter main option: "))

match option:
    case 1:
        engine_option = int(input("Enter engine option: "))
        match engine_option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Option Selected")
    case 2:
        lights_option = int(input("Enter lights option: "))
        match lights_option:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Option Selected")
    case 3:
        music_option = int(input("Enter music option: "))
        match music_option:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Track Selected")
            case 4:
                print("Previous Track Selected")
            case _:
                print("Invalid Option Selected")
    case 4:
        nav_option = int(input("Enter navigation option: "))
        match nav_option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Main Option Selected") 

##------------------------------------------------------------------------------------------------------------------##

# # question = 39 

role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Viewing Profile")
            case 2:
                leave_days = int(input("Enter number of leave days: "))
                if leave_days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("Viewing Salary")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Viewing Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Viewing Reports")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Role Selected ")

# ##------------------------------------------------------------------------------------------------------------------##

# # question = 40 

role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option Selected")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Students List")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option Selected")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Fees Management")
            case 2:
                print("Opening Admissions Portal")
            case 3:
                print("Opening Notices Board")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Role Selected")

# ##------------------------------------------------------------------------------------------------------------------##



