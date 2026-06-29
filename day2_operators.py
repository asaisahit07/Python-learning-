#arithmetic operators (+,-,*,/,%,//,**)
a=input("Enter first number:")
b=input("Enter second number:")
a=int(a)
b=int(b)
print("addition of the two numbers is",a+b)
sum=a+b
#similarly for *,/ and -
a=input("Enter first number:")
b=input("Enter second number:")
a=int(a)
b=int(b)
print("the double divison of a and b gives",a**b)
DD=a**b

#assignment operators (=,+=,-=,*=,/=,%=,**=,//=)
a=input("enter the value of a = ")
b=input("enter the value of b=")
a=int(a)
b=int(b)
a*=b
print("the value of a after the opetion is",a)
#similarly for other assignment operators

#rational operators (==,!=,>,<,>=,<=)
a=input("enter the value of a=")
b=input("enter the value of b=")
a=int(a)
b=int(b)
print("the result for a!=b is",a!=b)
print("the result for a>=b is",a>=b)

#logical operators (and,or,not) like in c ( && , || , ! )
a=input("enter the value of a=")
b=input("enter the value of b=")
a=int(a)
b=int(b)
print("the result on comparing a and b gives",a>b and a<b)
print("the result of comapring a and b gives", a>b or a<b)
print("the ccomparison of a nad b gvies", a>b and not a<b)

#bitwise operators (&,|,^,~,<<,>>)
a=input("enter the value of a =")
b=input("enter the value of b =")
a=int(a)
b=int(b)
print("the reusult of a&b is ",a&b)

#identity operators (is , is not)
a=input("ente the value of a =")
b=input("enter the value fo b =")
a=int(a)
b=int(b)
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

#membership operators (in , not in)
name=input("enter your name =" )
print("check if m is present in name or not\n", "m" in name)

list=input("enter the numbers=")
print("check if 1023 is present in the list or not\n", "1023" in list)