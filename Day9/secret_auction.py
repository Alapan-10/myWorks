import os
def clear():
    os.system('clear')

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

clear()
print(logo + "\nWelcome to the secret auction program.\n")
biddersLeft = True
allBids = {}
while biddersLeft:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    allBids[name] = bid
    moreBids = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if moreBids == "no":
        biddersLeft = False
    clear()

max = 0
for key in allBids:
    if allBids[key] > max:
        winner = key
        max = allBids[key]

print(f"The winner is {winner} with a bid of ${max}.")
