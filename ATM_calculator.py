pin=input("enter the pin=")
pin=int(pin)
balance=25000
if(pin!=1234):
    print("invalid pin\n")
else:
    print("the pin is correct\n")
debit=input("enter the amount to debit=")
debit=int(debit)
if(debit>balance):
    print("insufficiant funds in account")
elif(balance-debit<=1000):
    print("minimum balance is 1000 ")
elif(debit<=0):
    print("invalid amount entered")    
else:
    print("withdraw succesfull")
    balance-=debit
    print("the leftover balance is=",balance)