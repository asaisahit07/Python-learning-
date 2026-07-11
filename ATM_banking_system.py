#this program perform basic atm operations and it totally runs until the user chooses to exit the system 

balance=1000000
transaction=[]
choice=""
while choice!="5":
    print("------ATM MENU-------")
    print("1. check balance")
    print("2. withdraw amount")
    print("3. deposit money")
    print("4. view transaction history")
    print("5. exit system")
    
    choice=input("enter the choice = ")

    if(choice=="1"):
        print("the availabe balance is = ",balance)
        print("\n")

    elif(choice=="2"):
        withdraw_amount=int(input("enter the amount you want to withdraw = "))
        if(withdraw_amount>int(balance)):
            print("insufficient balance")
        elif(withdraw_amount<0):
            print("invalid amount entered")
        else:
            balance=int(balance)-withdraw_amount
            print("withdraw = ",withdraw_amount)
            print("balance",balance)
            transaction.append("withdrawl = " + str(withdraw_amount))
        print("\n")

    elif(choice=="3"):
        deposit_amount=int(input("enter the amount you want to deposit = "))
        balance=deposit_amount+int(balance)
        print("depoist = ",deposit_amount)
        print("balance = ",balance)
        transaction.append("deposition = " + str(deposit_amount))
        print("\n")

    elif(choice=="4"):
        print("the transaction histroy is \n",transaction)
        print("\n")

    elif(choice=="5"):
        print("thank you for choosing our bank and trusting us ! ")  
        break  