scores = input("Input a list of marks of students: ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
print(scores)

high = 0
for score in scores:
    if score > high:
        high = score
print(f"The highest score is: {high}")
