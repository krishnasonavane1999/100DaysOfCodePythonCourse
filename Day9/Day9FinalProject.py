from replit import clear
#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
secret_auction = {}
more_bidders = True

print(logo)
while more_bidders == True:
  clear()
  name = input("What is your name? ")
  bid = int(input("What is your bid$ "))

  secret_auction[name] = bid

  choice = input("Are there more bidders? Type 'yes' or 'no'")
  if choice == 'yes':
    more_bidders = True
  else:
    more_bidders = False


# find highest bid now
max_bid = 0
winner = ""

for person in secret_auction:
  secret_bid = secret_auction[person]
  if secret_bid > max_bid:
    max_bid = secret_bid
    winner = person

clear()
print(f"Winner of this auction is {winner} with ${max_bid}")
  
