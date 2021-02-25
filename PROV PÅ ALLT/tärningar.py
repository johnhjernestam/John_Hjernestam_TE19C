import random as rnd

femmor = 0

for x in range(10000):
    svar = rnd.randint(1,6)

    if svar == 5:
        femmor += 1
print(f"Det blev: {femmor} femmor")
