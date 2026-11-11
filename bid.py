
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of €{highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding == True:
    while True:
        name = input("What's your name?: ")
        if name and not any(character.isdigit() for character in name):
            break
        print("Please enter a name without numbers.")

    your_bid = int(input("What's your bid?: €"))
    bids[name] = your_bid
    should_continue = input("Any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 50)
