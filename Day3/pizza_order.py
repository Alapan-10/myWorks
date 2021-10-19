print("Welcome to Pykzzas!!")
size = input("What size pizza do you want? S, M or L ")
pep = input("Do you want pepperoni? Y or N ")
chez = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill += 15
elif size == "L":
    bill += 25
else:
    bill += 20

if pep == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if chez == "Y":
    bill += 1

print(f"Your total bill is {bill}$")

