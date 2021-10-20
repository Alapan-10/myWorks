import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator")
numLetters = int(input("How many letters would you like? "))
numSymbols = int(input("How many symbols would you like? "))
numNumbers = int(input("How many numbers would you like? "))

password = []

for i in range(0, numLetters):
    password.append(random.choice(letters))

for i in range(0, numSymbols):
    password.append(random.choice(symbols))

for i in range(0, numNumbers):
    password.append(random.choice(numbers))

for digit in range(0, len(password)):
    change = random.randint(0, len(password)-1)    
    password[digit], password[change] = password[change], password[digit]

finalPassword = ""
finalPassword = finalPassword.join(password)
print(finalPassword)
