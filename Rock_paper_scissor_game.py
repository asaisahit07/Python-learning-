ROCK=0
PAPER=1
SICSSOR=2
game=[0,1,2]
user_decision=int(input("enter one of these [0,1,2] ="))
import random
computer_decision=random.randint(0,2)
print("user decision =",user_decision)
print("computer decision =",computer_decision)
if(user_decision>2):
    print("invalid input given")
elif(user_decision==0):
    print("user choose ROCK")
elif(user_decision==1):
    print("user choose PAPER")
elif(user_decision==2):
    print("user choose SICSSOR")
if(computer_decision==0):
    print("computer choose ROCK")
elif(computer_decision==1):
    print("computer choose PAPER")
elif(computer_decision==2):
    print("computer choose SICSSOR")
print("---------GAME RESULT------------\n")

if(user_decision==0 and computer_decision==0):
    print("tie")
elif(user_decision==1 and computer_decision==1):
    print("tie")
elif(user_decision==2 and computer_decision==2):
    print("tie")
elif(user_decision==0 and computer_decision==1):
    print("computer won")
elif(user_decision==0 and computer_decision==2):
    print("user won")
elif(user_decision==1 and computer_decision==0):
    print("user won")
elif(user_decision==1 and computer_decision==2):
    print("computer won")
elif(user_decision==2 and computer_decision==0):
    print("computer won")
elif(user_decision==2 and computer_decision==1):
    print("user won")
elif(user_decision>2):
    print("no match conducted")