# #  Question = 1
# string = input("Enter any string : ")
# count = 0       # uppercase
# count1 = 0      # lowercase
# count2 = 0      # digits
# count3 = 0      # spaces
# count4 = 0      # special characters
# for i in string:
#     if i >= chr(65) and i <= chr(90):
#         count += 1
#     elif i >= chr(97) and i <= chr(122):
#         count1 += 1
#     elif i >= chr(48) and i <= chr(57):
#         count2 += 1
#     elif i == " ":
#         count3 += 1
#     else:
#         count4 += 1
# if count > count1 and count > count2 and count > count3 and count > count4:
#     print(f"Highest count is of uppercase letters, Count is: {count}")
# elif count1 > count and count1 > count2 and count1 > count3 and count1 > count4:
#     print(f"Highest count is of lowercase letters, Count is: {count1}")
# elif count2 > count and count2 > count1 and count2 > count3 and count2 > count4:
#     print(f"Highest count is of digits, Count is: {count2}")
# elif count3 > count and count3 > count1 and count3 > count2 and count3 > count4:
#     print(f"Highest count is of spaces, Count is: {count3}")
# elif count4 > count and count4 > count1 and count4 > count2 and count4 > count3:
#     print(f"Highest count is of special characters, Count is: {count4}")
# else:
#     print("Tie")

# ## Question = 2
# total1 = 0   #Excellent
# total2 = 0   #Good
# total3 = 0   #Pass 
# total4 = 0   #Fail
# for i in range (1,11) :
#     marks = int(input(f"Enter the marks of student : {i} is :"))
#     if 75 <= marks <= 100 :
#         total1 += 1
#         print("Excellent")
#     elif 50 <= marks <= 74 :
#         total2 += 1
#         print("Good")
#     elif 35 <= marks <= 49 :
#         total3 += 1
#         print("Pass")
#     else :
#         total4 += 1
#         print("Fail!!")

# print("total number of students are 10")
# print(f"Excellent student are : {total1}")
# print(f"Good students are : {total2}")
# print(f"Pass students are : {total3}")
# print(f"Fail!! students are : {total4}")

# ## Question = 3
# sentence = input("Enter any sentence :").lower()
# words = sentence.split()
# highest_score = 0
# for i in words :
#     score = 0 
#     for i in i :
#         if i == "aeiou":
#             score += 2
#         elif i == "bcdfghiklmnpqrstvwxyz":
#             score += 1
#         elif i == "0123456789":
#             score += 3
#         else:
#             score += 4
#     if score > highest_score :
#         highest_score = score
#         word = i
# print(word)

 
    
# ## Question = 4
# for i in range (1,6) :
#     i = input(f"Enter i - {i} :")
#     c1 = c2 = c3 = c4 = c5 =0
#     for j in i :
#         if len(j) >= 8 :
#             c1 = 1
#         elif j == j.isupper() :
#             c2 = 1
#         elif j == j.islower():
#             c3 = 1
#         elif j == j.isdigit() :
#             c4 = 1
#         else :
#             c5 = 1
#         conditions = 0
#     if len(j) > 8 :
#             conditions += 1
#     if c1 == 1:
#             conditions += 1
#     if c2 == 1 :
#             conditions += 1
#     if c3 == 1 :
#             conditions += 1
#     if c4 == 1 :
#             conditions += 1
#     if c5 == 1 :
#             conditions += 1
#     if (conditions) == 5 :
#             print("Strong i.")
#     elif (conditions) == 3 and (conditions) == 4 :
#             print("Medium i.")
    
# else :
#     print("Enter a valid i.")
   




# ## Question = 5
# sentence = input("Enter a sentence :").lower()
# words = sentence.split()
# total1 = total2 = total3 = 0
# for i in words :
#     print(f"for word  : {i} :")
#     print(f"Length of word {len(i)}")
#     if len(i) <= 3 :
#         total1 += 1
#         print("Short")
#     elif 4 <= len(i) <= 6 :
#         total2 += 1
#         print("Meadium")
#     elif len(i) > 6 :
#         total3 += 1
#         print("long")
# print(f"Number of short words : {total1}")
# print(f"Number of mesdium words : {total2}")      
# print(f"Number of long words : {total3}")


# ## Question = 6
# even = 0
# odd = 0
# for i in range (1,6):
#     num = (input(f"Enter the number {i} :"))
#     for j in num :
#         if int(j) % 2 == 0 :
#             even += 1
#         else :
#             odd += 1
# if  even > odd :
#     print(f"Even occurs more by : {even - odd} .")
# elif even == odd :
#     print(f"Both are equal ")
# else :
#     print(f"odd occurs more by : {odd - even} .")


## Question = 7










# ## Question = 8
# total1 = total2 = total3 = total4 =  0
# count1 = count2 = count3 = count4 = 0
# for i in range (1,9) :
#     prices = input(f"Enter price of product : {i}:")
#     if int(prices) >= 5000 :
#         count1 += 1
#         total1 = total1 + int(prices) 
#         print("Luxury")
#     elif 2000 <= int(prices) <= 4999 :
#         count2 += 1
#         total2 = total2 + int(prices)
#         print("Premium")
#     elif 500 <= int((prices)) <= 1999 :
#         count3 += 1
#         total3 = total3 + int(prices)
#         print("Regular")
#     else :
#         count4 += 1
#         total4 = total4 + int(prices)
#         print("Budget")
# print(f"Total amount : {(total1 + total2 + total3 + total4)}")
# print(f"Products in Luxury : {count1}")
# print(f"Products in Premium : {count2}")
# print(f"Products in Regular : {count3}")
# print(f"Products in Budget : {count4}")
# print(f"Average Product Price : {(total1 + total2 + total3 + total4) / 4}")


# ## Question = 9
# string = input("Enter a string :")
# count1 = count2 = count3 = count4 = 0
# for chr in string :
#     print(f"character is : {chr}")
#     position = string.index(chr)
#     print(f"position/indexing of chr is : {position}")
#     if position % 2 == 0 :
#         print("Position is even")
#     elif position % 2 == 1 :
#         print("Position is odd")
# for i in string:

#     if i.lower() in "aeiou":
#         count1 += 1
#         print("Character is vowel")

#     elif i.lower() in "bcdfghjklmnpqrstvwxyz":
#         count2 += 1
#         print("Character is consonant")

#     elif i in "0123456789":
#         count3 += 1
#         print("Character is digit")

#     else:
#         count4 += 1
#         print("Character is special character")    
# print(f"total characters which are vowel : {count1}")
# print(f"total characters which are consonant : {count2}")
# print(f"total characters which are digit : {count3}")
# print(f"total characters which are special characters : {count4}")


# ## Question = 10
# num = int(input("Enter a number :"))
# for i in range (1,num+1):
#     for j in range (1,i*2) :
#         if j % 15 == 0  :
#             print("Z",end=" ")
#         elif j % 3 == 0 :
#             print("X",end=" ")
#         elif j % 5 == 0 :
#             print( "Y", end=" ")
#         else :
#             print(j,end=" ")
#     print()

## Question = 11 
# for i in range (1,6) :
#     name = input(f"Enter username - {i} :") 
#     count1 = count2 = 0  
#     for j in name :
#         if  j.isdigit() :
#             count1 += 1
#         if j == chr(95) :
#             count2 += 1
#     if chr(33) <= j <= chr(47) or chr(58) <= j <= chr(64) or chr(91) <= j <= chr(96) :
#         print("Invalid")
#     elif count1 > 0 and count2 > 0 :
#         print("Needs to improvement.")
#     else :
#         print("Valid")
#     print(f"Length of name is : {len(name)}")
#     print(f"First letter of name is : {name[0]}")
#     print(f"Total digits is/are : {count1}")
#     print(f"Total underscores used : {count2}")


# ## Question = 12
# count1 = count2 = 0
# sentence = input("Enter a sentence :").lower()
# print(f"Vowel frequency of (a) - {sentence.count("a")}")
# print(f"Vowel frequency of (e) - {sentence.count("e")}")
# print(f"Vowel frequency of (i) - {sentence.count("i")}")
# print(f"Vowel frequency of (o) - {sentence.count("o")}")
# print(f"Vowel frequency of (u) - {sentence.count("u")}")
# for i in sentence :
#     for j in i :
#         if j in "aeiou":
#             count1 += 1
#         if j in "bcdfghjklmnpqrstvwxyz":
#             count2 += 1
# if count1 > count2 :
#     print(f"Vowel Wins .")
# elif count2 > count1 :
#     print(f"Consonants wins .")
# else :
#     print(f"Draw !!")


# ## Question = 13
# bill1 = bill2 = bill3 = bill4 = 0
# for i in range (1,7) :

#     unit = int(input("Enter unit usage by costomer-{i} :"))
#     if unit <= 100 :
#         bill1 = unit*5
#         print(f"Bill is- {bill1}")
#     elif 100 < unit <= 200 :
#         bill1 = 100*5
#         bill2 = (unit - 100)*7
#         print(f"Bill is- {bill1 + bill2}")
#     elif 200 < unit <= 400 :
#         bill1 = 100*5
#         bill2 = 100*7
#         bill3 = (unit - 200)*10
#         print(f"Bill is- {bill1 + bill2 + bill3}")
#     else :
#         bill1 = 100*5
#         bill2 = 100*7
#         bill3 = 200*10
#         bill4 = (unit - 400)*15
#         print(f"Bill is- {bill1 + bill2 + bill3 + bill4}")









# ## Question = 16
# password = input("Enter a password :")
# count1 = count2 = count3 = count4 = 0
# for i in password :
#     if i.islower() :
#         count1 += 1
#     elif i.isupper() :
#         count2 += 1
#     elif i.isdigit() :
#         count3 += 1
#     else :
#         count4 += 1
# a = len(password)
# print(f"The percentage of lower is - {(count1 / (a))*100}%")
# print(f"The percentage of upper is - {(count2 / (a))*100}%")
# print(f"The percentage of digit is - {(count3 / (a))*100}%")
# print(f"The percentage of special characters is - {(count4 / (a))*100}%")

# if count1 > 1 and count2 > 1 and count3 > 1 and count4 > 1 :
#     print("Strong password.")
# elif count1 > 1 and count2 > 1 and count3 < 1 and count4 < 1 :
#     print("Weak password.")
# else :
#     print("Medium password.")

# ## Question = 17
# for i in range (1,6):
#     name = (input(f"Enter name of student-{i} : ")).lower()
#     marks = int(input(f"Enter marks of students-{i} :"))
#     if 75 < marks <= 100 :
#         print("A")
#     elif 50 <= marks <= 75 :
#         print("B")
#     else:
#         print("fail")
#     count = count1 = 0
#     for j in name :
#         if j in "aeiou" :
#             count += 1
#         elif j in "bcdfghjklmnpqrstvwxyz" :
#             count1 += 1
#     print(f"Vowels in name is/are - :{count}"  )
#     print(f"Total characters in name are - :{len(name)}")
#     if count > count1 :
#         print(f"Vowels are more than consonents in this name ")
#     elif count1 > count :
#         print(f"consonents are more than vowel in this name ")
#     else :
#         print(f"vowel and consonents are equal :")
#################################### maximum mark of student ##################################################


## Question = 18
for i in range (1,8):
    print()
 

    







