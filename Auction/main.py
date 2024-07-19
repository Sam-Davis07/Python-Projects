from art import logo

print(logo)

dict_bid = {}

def highest(bidder_list):
    highest_bid = 0
    winner = ""
    for bidder in bidder_list:
        amount = bidder_list[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

ans = "yes"

while ans == "yes":
    name = input("Enter name:")
    bid_price = int(input("Enter Bid price: $"))
    dict_bid[name]=bid_price
    ans = input("Do you want to continue(yes/no):").lower()
    if ans != "yes":
        highest(dict_bid)
        break
    
