#round function use is to round of the float value to the nearest integer. It can also be used to round off to a specific number of decimal places by providing a second argument.
a=input("enter thte value of a =")
b=input("enter the value of b =")
a=float(a)
b=float(b)
print("the sum of the two numbers is = ",(a+b))
print(round(a+b,2))

#f-strings are a way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and formatted using the format() protocol.
#it is an easy and simple way to concatenate strings and variables together. It is also more readable and less error-prone than using the traditional string formatting methods.
name='SAHIT'
height='1.81'
age='19'
print(f"my name is {name} and my age is {age} , my height is {height} meters")

#if-else statments
a=int(input("enter the value of a ="))
b=int(input("enter the value of b ="))
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than a")

#nested if-else statements 
height=int(input("enter the height in m ="))
if(height>=3):
    print("you can ride the roller coaster")
    age=int(input("enter your age ="))
    if(age<=18):
        print("you cannot ride the roller coaster")
    else:
        print("you can ride the roller coaster")
else:
    print("you cannot ride the roller coaster")
    print("sorry for the inconvenience")        

#elif statements
height=int(input("enter the height in m ="))
if(height>=3):
    print("you can ride the roller coaster")
    age=int(input("enter your age ="))
    if(age<12):
        print("you need to pay 1500")
    elif(age>12 and age<=18):
        print("you need to pay 2000")
    elif(age>18 and age<=60):
        print("you need to pay 2500")
else:
    print("you cannot ride the roller coaster")
    print("sorry for the inconvenience")        
     
#multiple if statements
age=int(input("enter your age ="))
if(age<12):
    print("you need to pay 1500")
if(age>12 and age<=18):
    print("you need to pay 2000")
if(age>18 and age<=60):
    print("you need to pay 2500")   