 ## Question = 1 
i = 1
while i <= 5 :
    print("Hello")
    i += 1

## Question = 2 
i = 0
while i <= 9 :
    print(i,end=" ")
    i += 1

## Question = 3 
i = 1
while i <= 10 :
    print(i)
    i += 1


## Question = 4
i = 10 
while 1 <= i <= 10    :
    print(i)
    i -= 1

## Question = 5
i = 5
while i <= 50 :
    print(i)
    i += 5

## Question = 6
i = 2
while i <= 20 :
    print(i)
    i += 2

## Question = 7 
i = 1 
while i <= 19 :
    print(i)
    i += 2

## Question = 8
i = 3 
while i <= 18 :
    print(i)
    i += 3

## Question = 9
i = 20
while i >= 2 :
    print(i)
    i -= 2

## Question = 10
number = int(input("Enter a number :"))
i = 1
while i <= number :
    print(i)
    i += 1

## Question = 11
number = int(input("Enter a limit :"))
i = 2
while i <= number :
    print(i)
    i += 2

## Question = 12 
number = int(input("Enter a limit :"))
i = 1 
while i <= number :
    print(i)
    i += 2

## Question = 13
number = int(input("Enter a limit :"))
i = 1
while i <= number :
    if i % 3 == 0 :
        print(i)
    i += 1
    
## Question = 14
number = int(input("Enter a limit :"))
i = 1
while i <= number :
    if i % 2 == 0 and i % 3 == 0  : 
        print(f"number divisible by both 2 and 3 are : {i}")
    i += 1

## Question = 15 
number = int(input("Enter a limit :"))
i = 1
count = 0
while i <= number :
    if i % 2 == 0 :
        count += 1
    i += 1
print(f"Total number which are even : {count}")

## Question = 16 
number = int(input("Enter a number :"))
i = 1
while i <= number :
    i += i
print(i)


## Question = 17 
number = int(input("Enter a number :"))
i = 1
a = 0
while i <= number :
    if i % 2 == 0 :
        a += i
    i += 1
print(a)


## Question = 18 
number = int(input("Enter a number :"))
i = 1 
c = 0
while i <= number :
    if i % 2 == 1 :
        c += i
    i += 1
print(c)

## Question = 19 
number = int(input("Enter a number :"))
i = 0 
while i < 10 :
    i += 1
    print(i*number)

## Question = 20 
number = int(input("Enter a number :"))
i = 1 
a = 1
while i <= number :
    a *= i
    i += 1
print(a)


## Question = 21
string = input("Enter a string :")
i = 0 
while i < len(string) :
    print(string[i])
    i += 1


## Question = 22
string = input("Enter a string :")
i = 0 
while i < len(string) :
    print(string[i] , end=" ")
    i += 1


## Question = 23
string = input("Enter a string :")
i = 1
c = 0
while i <= 1 :
    print(f"Characters in string : {len(string)}")
    i += 1
    
    
## Question = 24
string = input("Enter a number :")
i = 0
c = 0 
while i < len(string) :
    if string[i] == "a" :
        c += 1
    i += 1
print(f"In string (a) occurs : {c} times")


## Question = 25
string = input("Enter a string :")
i = 0
c = 0
while i < len(string) :
    if chr(65) <= string[i] <= chr(94) :
        c += 1
    i += 1
print(f"In string uppercase letter : {c}")


## Question = 26
i = 0 
while i <= 2:
    j = 0
    print("*",end=" ")
    i += 1 
    while j <= 2 : 
        print("*",end=" ") 
        j += 1 
    print()


## Question = 27
i = 0
while i <= 3 :
    print("*",end="")
    j = 0 
    i += 1
    while j <= 4 :
        print("*",end="")
        j += 1 
    print()


## Question = 28
i = 0
while i <=  4 :
    i += 1
    j = 0
    while j < i :
        print("*",end=" ")
        j += 1
    print()


## Question = 29
i = 1
while i <= 5 :
    i += 1
    j = 1
    while j < i :
        print(j ,end=" ")
        j += 1
    print()
    

## Question = 30
i = 0
while i <= 4 :
    i += 1
    j = 1
    while j <=  10:
        print(j*i , end=" ")
        j += 1
    print()


## Question = 31
num = int(input("Enter a number :"))
i = 0
while i < num :
    i += 1
    j = 1 
    while j < i+1 :
        print(j,end=" ")
        j += 1
    print()



