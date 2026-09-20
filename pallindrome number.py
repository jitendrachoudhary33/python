################## PALINDROME ###################

# Take a number from user and check whether is it pallindrome or not .

num = int(input("Enter a atleast three digit number :"))
length = len(str(num))
# sum =0 
for i in range(length-1,-1,-1) :
    # sum = length + 1
    # if num == sum :
        print(f"{num} : is pallindrome")
# else :
#     print(f"{num} : is not pallindrome")