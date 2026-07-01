#this program will print the final bill afterall discounts and customizations


print("-----welcome to MVP booking site------\n")

user_age=int(input("enter your age ="))
print("user age is =",user_age)

print("--base price for tickets according to age category--\n")

if(user_age<0 or user_age>120):
    print("invalid age is choosen")
elif(user_age<12):
    print("category : child")
    ticket_price=150
    print("the ticekt price is =",ticket_price)
elif(user_age>=12 and user_age<=59):
    print("category : adult")
    ticket_price=250
    print("the ticekt price is =",ticket_price)        
elif(user_age>59 and user_age<=120):
    print("categroy : senior citizen")
    ticket_price=180
    print("ticket price is = ",ticket_price)

print("---discounts---\n")

if(user_age>=12 and user_age<=59):
    student=input("are you a student? (yes/no) :")
    student=student.lower()
    if(student=="yes"):
        print("you are eligible for extra 10% discount ")
        ticket_price=ticket_price-(ticket_price*(10/100))
        print("student discount is =",ticket_price*(10/100))
        print("the ticket price after student discount is =",ticket_price)
else:
    print("you are not eligible for student discount")

print("----customizations---")

snack=input("do you want to add snacks? (yes/no) :")
snack=snack.lower()
if(snack=="yes"):
    print("that would add extra 120 to the ticekt price")
    ticket_price=ticket_price+120
    print("the ticket price is =",ticket_price)
else:
    print("no snacks added")
    print("the ticket price is =",ticket_price)


print("----VIP upgradation----\n")

vip=input("do you want to upgrade to VIP? (yes/no) :")
vip=vip.lower()
if(vip=="yes"):
    print("the VIP upgrade would add extra 200 to the ticket price")
    ticket_price=ticket_price+200
    print("the ticket price is =",ticket_price)

print("----final bill----\n")
print("the final bill is =",ticket_price)


print("-------thank you for booking with us!-------")