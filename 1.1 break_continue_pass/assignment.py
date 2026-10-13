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




