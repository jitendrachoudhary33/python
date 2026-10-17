###-------------------------------------------------------------------------------------------

########  

# # question = 1 

# def welcome():
#     print("Welcome to python .")
# welcome()
# welcome()
# welcome()

# # question = 2 

# def greet(name):
#     return name 
# print(greet("jitesh"))

# # question = 3 

# def show_number(number) :
#     return number
# print(show_number(2))

# # question = 4 

# def add(a, b) :
#     return f" Addition is {a+b}"
# print(add(2,3))

# # question = 5 
   
# def square(number) :
#     return f"Square is {number**2}"
# print(square(3))

# # question = 6 

# def is_even(number) :
#     return number % 2 == 0
# print(is_even(4))

# # question = 7 

# def get_full_name(first_name, last_name) :
#     return f"Full name is {first_name}{last_name}"
# print(get_full_name("jitesh","choudhary"))

# # question = 8 

# def introduce(name, city="Pune") :
#     return name , city
# name, city = introduce("jitesh", "alwar")
# print(name,city)

# # question = 9 

# def subtract(a, b) :
#     return f"substraction is , {a-b}"
# print(subtract(3,4))

# # question = 10 

# def get_min_max(a, b) :
#     if a > b :
#         return f"{a} is max."
#     elif a == b :
#         return f"both are equal."
#     else :
#         return f"{b } is max."
# print(get_min_max(2,3))

# # question = 11 

# def calculate(a, b) :
#     sum = a + b 
#     difference = a - b 
#     multiplication = a * b 
#     division = (a / b )
#     return f"Addition is {sum} , substraction is {difference} , multiplication is {multiplication} , division is {division:.2f}."
# print(calculate(2,3))

# # question = 12 

# def count_digits(number) :
#     number = str(number)
#     count = len(number)
#     return count
# print(count_digits(1234))

# # question = 13 

# def classify_number(number) :
#     if number < 0 :
#         return "Negative "
#     elif number == 0 :
#         return "Zero"
#     else :
#         return "Positive "
# print(classify_number(0))

# # question = 14 

# def calculate_total(price, quantity=1) :
#     return f"Total price is {price*quantity}"
# print(calculate_total(3,4))

# # question = 15 

# def create_email(username, domain="example.com") :
#     return f"{username} , {domain}"
# print(create_email("jitesh","jitendra.choudhary.cg@gmail.com"))

# # question = 16 

# def format_name(first, last, uppercase=False) :
#     if uppercase == True :
#         first = first.upper()
#         last = last.upper()
#     return f"{first},{last}, {uppercase}"
# print(format_name("jitesh", "choudhary",True))

# # question = 17 

# def percentage(marks, total=100) :
#     return f"Pecentage is {(marks/100)*100}%"
# print(percentage(90))

#  # question = 18 

# def convert_minutes(minutes, seconds_per_minute=60) :
#     return f"Total seconds is {minutes*60}"
# print(convert_minutes(2))

# # question = 19 

# def student_details(name, age, city) :
#     return f"Name is {name},Age is {age},city is {city}"
# print(student_details("jitesh",22 , "Pune"))

# # question = 20 

# def bill(item, quantity=1, price=100) :
#     return f"Item = {item}, Quantity = {quantity} , Price = {price*quantity} "
# print(bill("Clothes",2))

# # question = 21 

# def analyze_number(number) :
#     number = number*(-2)+(number)
#     if number % 2 == 0 :
#         print("Even")
#     else :
#         print("Odd")
#     return number 
# print(analyze_number(-4))

# # question = 22 

def  calculate_stats(a, b, c) :
    if a > b and a > c :
        print(f"{a} is greater number .")
    elif b > a and b > c :
        print(f"{b} is greater number .")
    else :
        print(f" all are equal ")
    return 

