#this program is about the silent auction system where the user can bid for the items and the highest bidder will win the item

print("---------WELCOME TO THE SILENT AUCTION SYSTEM-----------")
print("\n")
bidders={}
def bidder():
    while True:
        bidder_name=input("enter your name please : ").lower()
        if bidder_name in bidders:
            print("the bidder name is already present please try to enter with your specific name or initial : ")
            continue
        bid_amount=int(input("enter your bid here please : "))
        if bid_amount<=0:
            print("the amount is invalid please enter a valid amount : ")
            continue
        bidders[bidder_name]=bid_amount

        print("are there any bidders left ? (yes/no) : ")
        choice=input().lower()
        if choice=='no':
            break
        elif choice=='yes':
            continue
        else:
            print("invalid choice please enter yes or no : ")
            continue
bidder()
highest_bid=max(bidders.values())
for i in bidders:
    if bidders[i]==highest_bid:
        print("the winner is ",i,"with the bid amlount of ",highest_bid)
print(bidders)