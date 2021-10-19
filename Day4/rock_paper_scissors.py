import random

choose = ['''
    ____
___|  __)___
       (____)
       (____)
___    (____)
   |__(__)
''',  '''
    _____
___|  ___)______
        ________)
        ________)
___    _________)
   |_______)
''',  '''
    ____
___|  __)_______
        ________)
        ________)
___    (____)
   |__(__)
'''
]

you = -1
while( you < 0 or you > 2):
        you = int(input("What do you choose? 0 for Stone, 1 for Paper or 2 for Scissor. " ))

print(f"You Choose {choose[you]}")
comp = random.randint(0, 2)
print(f"Computer Choose {choose[comp]}")

if you == comp:
    print("It's a draw")
else:
    if you == 0:
        if comp == 1:
            print("You lose")
        else:
            print("You win")
    elif you == 1:
        if comp == 2:
            print("You lose")
        else:
            print("You win")
    else:
        if comp == 0:
            print("You lose")
        else:
            print("You win")   
