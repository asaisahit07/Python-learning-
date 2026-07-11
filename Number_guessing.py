#this program randomly generates a nmber btw 1 to 100 and user has to guess the number . the user has infinite no.of attempts

print("----------Welcome to Guessing game---------")
import random
number=random.randint(1,100)
attempt=0
user_guess=""
while user_guess!=number:
    user_guess=int(input("enter your guess number = "))
    print("\n")
    if(user_guess>100 or user_guess<1):
        print("invalid number ! try only between 1 to 100")
        print("\n")
    elif(user_guess<number):
        print("too low,try higher numbers")
        attempt+=1
        print("\n")
    elif(user_guess>number):
        print("too high,try lower numbers")
        attempt+=1
        print("\n")
    elif(user_guess==number):
        print("congratulations! you've guessed right")
        attempt+=1
        print("number of attempts taken = ",attempt) 
        print("\n")
        break 
if(attempt<5):
    print("excellent")
    print("\n")
elif(attempt>=5 and attempt<10):
    print("good")
    print("\n") 
else:
    print("keep practicing")   
    print("\n")
print("-----------thank you for playing!-----------")                  