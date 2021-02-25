import math

x1 = float(input("Ange ett värde mellan -3 och 3: "))
y1 = float(input("Ange ett värde mellan -3 och 3: ")) 
x2 = float(input("Ange ett värde mellan -3 och 3: "))
y2 = float(input("Ange ett värde mellan -3 och 3: ")) 

def avstånd(x1, y1, x2, y2):
    avstånd = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return avstånd

s = avstånd(x1, y1, x2, y2)
print(f"{s:.3f}")