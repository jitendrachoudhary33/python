###------------------------------------------------------------------------------------------------------------##
 
# question = 1 

def greet():
    print("Hello")

print("Start")

#########   OUTPUT = Start ############

# question = 2 

def greet():
    print("Hello")

greet()
greet()

#########   OUTPUT = Hello Hello  ############

# question = 3 

def first():
    print("A")

def second():
    print("B")

second()
first()
second()

#########   OUTPUT = B A B   ############

# question = 4 

def show():
    print("Inside")

print("One")
show()
print("Two")
show()

#########   OUTPUT = One Inside, Two Inside  ############

# question = 5 

def outer():
    print("Start")
    print("Middle")

print("A")
outer()
print("B")

#########   OUTPUT = A Start Middle B  ############

# question = 6 

def task():
    print("Task")

task
print("Done")

#########   OUTPUT = Done  ############

# question = 7 

def greet():
    print("Hello")

greet()

#########   OUTPUT = Name-Error  ############

# question = 8 

def show():
    print("A")
    print("B")

print("C")
show()

#########   OUTPUT = C A B  ############

# CODING PRACTICE PROBLEMS 

# BASIC LEVEL 

# question = 1 

def greet() :
    print("Hllo,python!")
greet()

# question = 2 

def print_name (name) :
    return name
print(print_name("jitesh"))
print(print_name("aryan"))

# question = 3 

def print_line():
    print("_____________________________________")
print_line()

# question = 4 

def show_rules():
    print("Rule 1")
    print("Rule 2")
    print("Rule 3")
show_rules()

# question = 5 

def show_squre(num) :
    print(f"Squre is : {num*num}")
show_squre(4)

# question = 6 

def show_menu ():
    print("1. burger")
    print("2. pizza")
    print("3. momoj")
show_menu()

# question = 7 

def morning_massage() :
    print("Good morning ")
def evening_massage() :
    print("Good evening")
evening_massage()
morning_massage()

# question = 8 

def show_student_card (name,rollnumber) :
    print("STUDENT CARD !!")
    return name , rollnumber
name,rollnumber = show_student_card("jitesh",23)
print(name,rollnumber)

# question = 9 

def print_number():
    for j in range(1,6):
        print(j)
print_number()

# question = 10 

def show_pattern():
    for i in range (1,4) :
        for j in range (1,i+1):
            print("*",end=" ")
        print()
show_pattern()

######     INTERMEDIATE LEVEL ############## 

# question = 11 

def show_header () :
    print("header")
def show_body ():
    print('Body')
def show_footer() :
    print("Footer")
print("Report")
show_header()
show_body()
show_footer()

# question = 12 
 
def  show_separator():
    print("====================")
show_separator()

# question = 13 

def step_one() :
    print("step one ")
def step_two() :
    print("Step two")
def step_three():
    print("Step three")
step_three()
step_two()
step_one()

# question = 14 

def show_table_heading() :
    print("Column heading")
    print("1.daksh")
    print("2.neel")
show_table_heading()

# question = 15 

def five_star ():
    for i in range (5) :
        print("*",end=" ")
five_star()

# qiestion = 16 

def show_help () :
    print("Calculator menu ")
    print("Rule 1")
    print("Rule 2")
    print("Rule 3")
    print("Rule 4")
show_help()

# question = 17 

def show_welcome() :
    print("Welcome to coding gita ")
show_welcome()

# question = 18 




# question = 19 

def print_box():
    print("""--------------
             ----------------
            -----------------""")
print_box()
print_box()

# question = 20 

# def programe_title () :

#########  DEBUGGING AND REASONING ########### 

# question = 21 

def greet():
    print("Hello")
greet()

# question = 22 

def welcome():
    print("Welcome")
welcome()

# question = 23 

def show():
    print("Hello")
show()

# question = 24 

def print_report():
    print("Report")
print_report()

# question = 25 

def a():
    print("A")
def b():
    print("B")
a()
b()
a()

# question = 26 

def message():
    print("Python")
message()
message()
message()
message()

###### OUTPUT = python python python python  #######

# question = 27 

def example():
    print("One")
    print("Two")

print("Three")

######  Function body = print("one"), print("Two")

# question = 28 

## rename =
### do_task
### student_details 
### x1

# question = 29 

def add(a,b):
    return a + b 
def sub(a,b):
    return a - b 
print(add(3,4))

# question = 30 

def print_massage ():
    print("hllo")
print_massage()
print("jitesh")


