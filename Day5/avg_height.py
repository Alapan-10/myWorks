heights = input("Input a list student heights: ").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])
print(heights)

sum = count = 0
for h in heights:
    sum += h
    count += 1

print(f"The average height is: {sum/count}")
