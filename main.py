from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

def find_higgest_bidder(bids, count):
  auction_list = list(bids.items()) 
  highest_name = auction_list[0][0]
  highest_bid = auction_list[0][1]
  if count > 1:
    for n in range(1, len(auction_list)):
      if auction_list[n][1] > highest_bid:
        highest_name = auction_list[n][0]
        highest_bid = auction_list[n][1]
  print(f"Highest bidder is {highest_name} with the bid of ${highest_bid}!")

print(logo)
print("Welcome to the secret auction program.")
auction_dic = {}
count = 0
while True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction_dic[name] = bid
  count += 1
  answer = input("Are there any other bidder? Type 'yes' or 'no'. ").lower()
  if answer == 'yes':
    clear()
  else:
    break

find_higgest_bidder(auction_dic, count)  