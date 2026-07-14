#function declaraton and calling 

def greet():
    print("hi! sahit")
greet()
#the number of times you call the function , it will print it that many times

def findmax():
    a=10
    b=20
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
findmax()            



def calculate_bill():
    quantity=int(input("enter the quantity ="))
    bill=0
    if(quantity<5):
        print("bill is 500")
        bill=500
        print(bill)
    else:
        print("bill is 1000")
        bill=1000 
        print(bill)   
calculate_bill()


def add(a,b):
    c=a+b
    print("the sum is = ",c)
add(90,9)    