## METHOD = 1
string = input("Enter a string : ")
rstring = ""
i = len(string) - 1
while i >= 0 :
    rstring = rstring + string[i]
    i -= 1
if  string == rstring :
    print("pallindrome")
else :
    print("not pallindrome") 



## METHOD = 2

string = input("Enter a string :")
i = 0
j = len(string) - 1
flag = True 
while i < j :
    if string[i] == string[j] :
        i += 1
        j -= 1
    else:
        flag = False 
        i = j
if flag == True :
    print("pallindrme")
else :
    print("not pallindrome")


## METHOD = 3


string = input("Enter a string :")
i = 0
j = len(string) - 1
flag = True 
while i < j and flag:
    if string[i] == string[j] :
        i += 1
        j -= 1
    else:
        flag = False 
if flag == True :
    print("pallindrme")
else :
    print("not pallindrome")


# METHOD = 4


string = input("Enter a string :")
i = 0
j = len(string) - 1
flag = False 
while i < j :
    if string[i] != string[j] :
        i += 1
        j -= 1
    else:
        flag = True
        i = j
if flag == True :
    print("pallindrme")
else :
    print("not pallindrome")









