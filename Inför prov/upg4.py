import math 

x = float(input("Skriv ett värde på x: "))

y = float(input("Skriv ett värde på y: "))

x2 = float(input("Skriv ett värde på x: "))

y2 = float(input("Skriv ett värde på y: "))

disx = x2-x

disy = y2-y

avstånd = math.sqrt(disx**2+disy**2)

print(avstånd)

