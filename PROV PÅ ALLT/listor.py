import random as rnd

tärningskast = []

for k in range(10):
    kast = rnd.randint(1,6)
    tärningskast.append(kast)
    tärningskast.sort()
print(tärningskast)



