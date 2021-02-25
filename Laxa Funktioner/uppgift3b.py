import math
import random as rnd

x1 = rnd.uniform(-3,3) 
y1 = rnd.uniform(-3,3)
x2 = rnd.uniform(-3,3) 
y2 = rnd.uniform(-3,3)
print("(x1,y1) = (",x1,",", y1,")" ) 
print("(x2,y2) = (",x2,",", y2,")" ) 

def avstånd(x1, y1, x2, y2):
    avstånd = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return avstånd

s = avstånd(x1, y1, x2, y2)
print(f"{s:.3f}")

