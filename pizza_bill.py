#mini project 2 
#this code gives the bill of pizza based on the size of pizza and add ons like extra cheese and pepperoni.


size=input("what size of pizza do you want? S, M or L =")
size=str(size)
if(size=='S'):
    bill=100
    print("the bill is =",bill)
elif(size=='M'):
    bill=200
    print("the bill is =",bill)
else:
    bill=300
    print("the bill is =",bill)

addpepperoni=input("do you want pepperoni? Yes or No =")    
addpepperoni=str(addpepperoni)
if(addpepperoni=='Yes'):
    if(size=='S'):
        bill+=20
        print("the bill is =",bill)
    elif(size=='M' ):
        bill+=50
        print("the bill is =",bill)
    else:
        bill+=70
        print("the bill is =",bill)
else:
    print("the bill is =",bill)

addcheese=input("do you want extra cheese? Yes or No =")
addcheese=str(addcheese)
if(addcheese=='Yes'):
    bill+=30
    print("the  final bill is =",bill)
else:
    print("the  finalbill is =",bill)             