import os


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bid winner is {winner}, with bid amount of {highest_bid}!")


bids = {}


while True:
    print("Welcome to secret auction!")
    name = input("What is your name?\n")
    bid = int(input("What is your bids?\n$"))
    bids[name] = bid
    other_user = input("Are there any other bidders? 'Yes' or 'No'\n").lower()
    if other_user == "no":
        find_highest_bidder(bids)
        break
    elif other_user == "yes":
        clear_screen()
