import random as rnd

siffror = {}

for i in range(1,10):
    slumptal = rnd.randint(1,6)
    siffror[f"{i}"] = slumptal
    
print(siffror)
