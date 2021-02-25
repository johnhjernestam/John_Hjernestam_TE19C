import random as rnd

femmor = 0

for k in range(10000):
    x = rnd.randint(1,6)

    if x == 5:
        femmor += 1
print(f"Så många femmor blev det: {femmor}")






