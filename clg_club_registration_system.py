#this is a club registration system for GMRIT students. The system will take the student's name, age, branch, year of study, and club choice as input. It will then calculate the registration fee based on the year of study and apply any applicable discounts. The system will also allow the student to customize their starter pack and enter their skills. Finally, the system will randomly select a lucky draw prize for the student and print out a registration bill with all the details.

print("---------welcome to GMRIT clubs registration system------------\n")
name=input("enter your full name = ")
age=int(input("enter your age = "))
if(age<17 or age>30):
    print("you are not eligible to register for any club")
    exit()
branch=input("enter your branch = ")
year=int(input("enter your year of study = "))

available_clubs=("coding club", "dance club", "music club", "photography club", "sports club", "ai club")
print("available clubs are : ")
print("1",available_clubs[0])
print("2",available_clubs[1])
print("3",available_clubs[2])
print("4",available_clubs[3])
print("5",available_clubs[4])
print("6",available_clubs[5])
club_choice=int(input("enter the number of the club you want to register in = "))
if(club_choice<1 or club_choice>6):
    print("invalid club choice")
    exit() 
print("\n")

print("------registration fee-------\n")


if(year==1):
    print("the registration fee is 300")
    registration_fee=300
elif(year==2):
    print("the registration fee is 500")
    registration_fee=500
elif(year==3):
    print("the registration fee is 700")        
    registration_fee=700    
elif(year==4):
    print("the registration fee is 900")
    registration_fee=900
print("\n")


print("--------discount details--------\n")


if(club_choice==1 or club_choice==6):
    print("you are eligible for 15% discount")
    discount=registration_fee*0.15
    final_fee=registration_fee-discount
    print("the discount amount is = ",discount)
    print("the final fee after discount is = ",final_fee)
else:
    print("you are not eligible for the discount")
    discount=0
    final_fee=registration_fee
print("\n")    

print("------starter pack details-------\n")

starter_pack=["ID card", "note-book", "pen"]
water_bottle=input("do you want to add water bottle to your starter pack? (yes/no) = ")
club_tshirt=input("do you want to add club t-shirt to your starter pack? (yes/no) = ")
if(water_bottle=="yes"):
    starter_pack.append("water bottle")
if(club_tshirt=="yes"):
    starter_pack.append("club t-shirt")
print("\n")
print("your starter pack includes: ", starter_pack)
print("\n")
skills=input("enter your skills separated by comma = ")
skills_list=skills.split(",")
print("\n")
print("your skills are: ", skills_list)
print("\n")

import random
lucky_draw=random.choice(["smart watch", " wireless headphones", "poer bank", "backpack", "coffee mug", "no prize"])
print("\n")
print("the lucky draw prize is: ", lucky_draw)  
if(lucky_draw=="no prize"):
    print("better luck next time")  
print("\n")    


print("----------------------------------------------------------------")
print("                     registraion bill                  ")
print("----------------------------------------------------------------\n")
print("  name : ", name)
print("  age : ", age)
print("  branch : ", branch)
print("  year of study : ", year)
print("  club registered : ", available_clubs[club_choice-1])
print("  registration fee : ", registration_fee)
print("  discount amount : ", discount)
print("  final fee after discount : ", final_fee)
print("  starter pack : ", starter_pack)
print("  skills : ", skills_list)
print("  lucky draw prize : ", lucky_draw)
print("  thank you for registering for the club, have a great day!")