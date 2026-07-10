#this program is a game where the user can play a carnival game and win prizes based on their luck. The program prompts the user to enter their name and age, and then generates a random number to determine the outcome of the game. The user can win different prizes based on the number generated, and the program prints the final result to the console.

print("-----welcome to GMRIT lucky carnival game------\n")


name=input("ente your name = ")
branch=input("enter your branch = ")
year_of_study=int(input("enter your year of study = "))
print("\n")


import random
lucky_number=random.randint(1,10)


print("the user has 3 attempts to guess the lucky number between 1 and 10\n")
for attempt in range(1,4):
    user_guess=input("enter your guess = ")
    print("attempt number = ",attempt)
    if(user_guess==lucky_number):
        print("congratulations ",name,"! you have guessed the correct number and won a prize!")
        prize_list=["smart watch","headphones","coffee mug","bluetooth speaker","backpack"]
        lucky_prize=random.choice(prize_list)
        print("the prix]ze you've won is = ",lucky_prize)
        break
    else:
        print("sorry ",name,"! you have guessed the wrong number. Please try again.\n")
print("the lucky number is = ",lucky_number)
print("\n")        

print("------------thank you for participating in the carnival!----------------\n ")