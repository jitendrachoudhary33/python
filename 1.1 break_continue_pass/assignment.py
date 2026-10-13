#------------------------------------------------------------------------------------------------------------------##

# question = 1 

for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")

# ## OUTPUT IS 1, 2 , 3 , 4 ,FINISHED ....

# question = 2 

word = "skyline"
for ch in word:
    if ch in "aeiou":
        break
    print(ch)

# ## OUTPUT IS s, k y, l ....

# question = 3 

n = 2
while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

# ## OUTPUT IS 2 , 4 , 6  ....

# question = 4 

i = 1 
limit = int(input("Enter a limit : "))
while i <= limit :
    if i == 7 :
        break 
    print(i)
    i+=1

# question = 5 

string = (input("Enter a string : ")).lower().strip()
target = input("Enter target letter : ").lower().strip()
for ch in string :
    if ch == target :
        print(ch)
        break
    print(ch , end="")
    
# question = 6 

numbers = input("Enter nnumber in a line with space : ").split( )
for num in numbers :
    if int(num) < 0 :
        break
    print(num)

# question =  8

sentence = input("Enter a sentence : ").split()
target = input("Enter target word : ")
for ch in sentence :
    if ch == target :
        print("Found !!")
        break 
else :
    print("Not Found !!")

# question = 9 

for i in range(1, 7):
    if i == 4:
        continue
    print(i)
# # # ###########  OUTPUT = 1,2,3,5,6 


# question = 10 

for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")

# # # ###########  OUTPUT = dctn

# question = 11 

n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# # # # ###########  OUTPUT = 1 ,2 , 4 , 5


# question = 12 

num = int(input("Enter a number : "))
for i in range (1, num+1):
    if i % 3 == 0 :
        continue 
    print(i)

# question = 13 

string = input("Enter a string : ")
target = input("Enter a target charecter : ")
for ch in string :
    if ch == target :
        continue 
    print(ch,end="")

# question = 14 

marks = input("Enter marks in a line with a space : ").split()
passing_limit = (input("Enter passing limit : "))
for num in marks :
    if (num) < passing_limit :
        continue
    print(num)

# question = 15 

for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)

#### ### SKIP OUTPUT = A2 , B2 

# question = 16 

n = 0
while n < 5:
    if n == 3:
        n += 1
        continue
    n += 1
    print(n)

# question = 17 

count = 0 
string = input("Enter a string : ").lower()
for ch in string :
    if ch in "aeiou" :
        continue
    else:
        count += 1
print(count)

# question = 18 

for i in range(1, 4):
    print(i)
else:
    print("Done")

## ####### OUTPUT = 1,2,3 ,Done

# question = 19 

for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

## ####### OUTPUT = 1,3,4,Completed 

# question = 20 

for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")

## ####### OUTPUT = 1,2,Outside loop

# question = 21 

for item in []:
    print("Inside")
else:
    print("Else block")

## ####### OUTPUT = Else block 

# question = 22 

numbers  = input("Enter  number in a line with space : ").split()
print(numbers)
target = input("Enter target number : ")
for num in numbers :
    if num == target :
        print("Found !! ")
        break
else :
    print("Not Found !! ")


# question = 23 

string = input("Enter a string : ")
target = input("Enter a target letter : ")
for ch in string:
    if ch == target :
        print("Charecter exists ")
        break
else :
    print("Charecter does not exist ")

# question = 24 

num = int(input("Enter a number : "))
for i in range (2, num ):
    if num % i == 0 :
        print("Not prime !!")
        break 
else :
    print("Prime !!")

# question = 25 

values = [2, 4, 6, 8]

for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")

############# OUTPUT == "All are even "

# question = 27 

count = 0 
str = ""
string = input("Enter a string : ")
for ch in string :
    if ch in str :
        print(ch)
        print("Repeated character found !! ")
        break
    str += ch
else :
    print("No Repeated Character !! ")

# question = 28 

for i in range(1, 4):
    if i == 2:
        pass
    print(i)

####### OUTPUT = 1,2,3  ################

# question = 29 

x = 10
if x > 5:
    pass
print("Finished")

############ OUTPUT = Finished ############

# question = 30 

for letter in "cat":
    pass
print("Loop ended")

##### ############# OUTPUT = Loop ended ############

# question = 31 

for i in range (1, 6):
    if i % 2 == 0 :
        pass
    print(i)

# question = 32 





# question = 33

for i in range(1, 5):
    if i == 3:
        pass
    print(i)


##### ############# OUTPUT = 1,2,3,4   ########## 

for i in range(1, 5):
    if i == 3:
        continue
    print(i)

##### ############# OUTPUT = 1,2, 4   ########## 

# question = 34 

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# question = 35 

for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")

##### OUTPUT = 1,3   #############

# question = 36 

list = input("Enter number in a line using space : ").split()
target = input("Enter target number : ")
for num in list :
    if int(num) < 0 :
        continue
    if num == target :
        print("Target found !!")
        break
else :
    print("Target not found !!")

# question = 37 

list = input("Enter number in a line using space : ").split()
for num in list :
    if int(num) == 0 :
        continue
    if int(num) == -1 :
        break
    print(num)
else :
    print("All values processed")

# question = 38 

for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

######### OUTPUT = (1,1), (1,3) ,"All values processed", (2,1) , (2,3) ,"All values processed" ################

# question = 39 

list = input("Enter number in a line with space : ").split()
for num in list :
    if int(num) < -1 :
            continue
    if int(num) % 4 == 0 and int(num) % 6 == 0 :
        print("Found , number is :",num )
        break
else :
     print("No matching number exists.")

# question = 40 

# |1 | = | break |
# | 2 | = | continue |
# | 3 | = | for-else |
# | 4 | = | pass |
# | 5 | = | continue |
# | 6 | = | break |
# | 7 | = | for-else |
# | 8 | = | pass |