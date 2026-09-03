# Task=1
my_name="jitesh"
city="alwar"
favorite_promming_language="python"
print(my_name,city,favorite_promming_language)
# Task=2
a="   "
print(a)
print(len(a))
print(type(a))
# Task=3
a="Python Programming"
print(a)
print(len(a))
print(a[0])
print(a[-1])
print(a[2])
print(a[-2])
# Task=4
a="programming"
print(a[0])
print(a[1])
print(a[6])
print(a[-1])
# Task=5
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-11])
# Task=6
a="jitesh choudhary"
print(a[0])
print(a[-1])
print(a[7])
# Task=7
a="Python Programming"
print(a[:6])
print(a[7:])
print(a)
print(a[:5])
print(a[-5:])
# Task=8
a="ABCDEFGHIJKL"
print(a[::2])
print(a[::3])
print(a[1:8:2])
print(a[::-1])
# Task=9
a="Python Programming"
print(a[-5:])
print(a[-10:])
print(a[::-1])
# Task=10
a="programming"
print(a[:3])
print(a[-3:])
print(a[::2])
print(a[-1])
print(a[1:10])
# Task=11
a="python"
b="pyhtonprogramming"
c="my fevorite language is python"
print(len(a))
print(len(b))
print(len(c))
# Task=12
text="Python Programming"
print(len(text))
print(text[17])
# Task=13
first_name="jitesh"
last_name="choudhary"
print(first_name + " " + last_name)
# Task=14
Name="jitesh"
Age=19
City="alwar"
Programming_language="python"
print(Name +str(Age)+City+Programming_language)
# Task=15
#print(5+"guild")
# type error occurs
print(str(5)+"guild")
# Task=16
a="Hlo "
print(a*3)
print(a*5)
print(a*10)
# Task=17
a="*"
print(a*10)
# Task=19
a="python programming language"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())
# Task=20
a="Python is a programming language"
b="python" in a 
c="programming" in a
d="java" in a
e="language" in a
print(b,"\n",c,"\n",d,"\n",e,)
# Task=21
a="Python is a programming language"
b=a.find("python")
c=a.find("programming")
d=a.find("language")
e=a.find("java")
print(b,"\n",c,"\n",d,"\n",e,)
# Task=22
a="Python is a programming language"
b=a.index("Python")
c=a.index("programming")
d=a.index("language")
#e=a.index("java")
print(b,"\n",c,"\n",d,"\n",e,)
# Task=23
a="banana"
b=a.count("a")
c=a.count("b")
d=a.count("n")
print(b,"\n",c,"\n",d,)
# Task=24
file_name="student_notes.pdf"
a=file_name.startswith("student")
b=file_name.endswith(".pdf")
c=file_name.endswith(".txt")
print(a,"\n",b,"\n",)
# Task=25
text="I am learning Java"
b=text.replace("Java","Python")
print(b)
# Task=26
text="apple apple apple"
b=text.replace("apple","mango")
print(b)
# Task=27
text="apple apple apple"
b=text.replace("apple","mango",1)
print(b)
# Task=28
text="python"
b=text.upper()
print(text)
print(b)
# Task=29
text=" Python Programming "
b=text.strip()
c=text.lstrip()
d=text.rstrip()
print(b,"\n",c,"\n",d)
# Task=30
name = input("Enter your name:")
name = name.strip()
print(name)
# Task=31
text="Python is easy to learn"
print(text.split())
# Task=32
fruits="apple,banana,mango,orange"
a=fruits.split()
print(a)
# Task=33
words=["Python","is","easy"]
a=" ".join(words)
print(a)
# Task=34
words=["Python","is","easy"]
a="_".join(words)
print(a)
# Task=35
name="jitesh"
age=19
city="alwar"
a= f"My name is {name}. I am {age} years old. I am from {city}"
print(a)
# Task=36
a=10
b=20
c=a+b
d=f"The Sum is {c}."
print(d)
# Task=37
# A
text="python"
# print(text[20])
 # B
text = "Python"
b= "J"+text[1:]
print(b)
# C
age = 20
print("Age: " + str(age))
# D
text = "Python"
print(text.find("Java"))
