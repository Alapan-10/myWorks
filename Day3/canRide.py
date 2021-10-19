print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You are Welcome!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age > 18:
        if (age >= 45 and age <= 55):
            crisis = True
        else:
            bill = 12
    else:
        bill = 7
    pic = input("Do you want a photo? Y or N ")
    if (crisis == True):
        print("Hevy Relax, Enjoy Free Ride")
    else:
        if pic == "Y":
            print(f"Your total bill is {bill + 3}$")
        else:
            print(f"Your total bill is {bill}$")
else:
    print("Sorry, you cannot ride")
