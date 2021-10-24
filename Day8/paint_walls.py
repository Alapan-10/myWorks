import math

def calCans(h, w, c):
    area = h * w
    numOfCans = math.ceil(area / c)
    print(f"The number of cans required is {numOfCans}.")

height = float(input("Enter the height of wall in metres: "))
width = float(input("Enter the width of wall in metres: "))
coverage = 5

calCans(w = width,c = coverage, h = height)
