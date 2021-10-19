print("Welcome to Treasure Island \n Your Mission is to find the treasure")

decision = input("Do you want to go left or right? ").lower()
if decision == "left":
    decision = input("Do you want to swim or wait? ").lower()
    if decision == "wait":
        decision = input("Which door do you choose Red, Blue or Yellow? ").lower()
        if decision == "yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
