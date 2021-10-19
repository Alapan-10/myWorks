print("Welcome to L Calculator")
p1 = input("Enter name of first person: ").lower()
p2 = input("Enter name of second person: ").lower()
a = 0
b = 0
for x in range (4):
    for y in p1:
        if( "true"[x] == y ):
            a = a + 1
        if( "love"[x] == y ):
            b = b + 1
    for y in p2:
        if( "true"[x] == y ):
            a = a + 1
        if( "love"[x] == y ):
            b = b + 1

result = int(str(a) + str(b))
if (result <= 10 or result >= 90):
    print(f"Result is {result}%, Like coke and mentos")
elif (result >= 40 and result <= 50):
    print(f"Result is {result}%, Perfectly Balanced")
else:
    print(f"Result is {result}%")
