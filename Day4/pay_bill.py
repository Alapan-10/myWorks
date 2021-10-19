import random

names = input ("Enter everybody's name seperated by comma: ").split(", ")
print (f"{names[random.randint(0,len(names)-1)]} will pay the bill.")
