import random as rnd

dices = []
dices_sorted = []
antal_femmor = 0

with open("diceRoll.txt", "w") as f1:
    for i in range (10):
        kast = rnd.randint(1,6)
        dices.append(kast)
        dices_sorted.append(kast)
        dices_sorted.sort()
        if kast == 5:
            antal_femmor += 1

    f1.write(f"Simulera 10 tarningskast: {dices} ")
    f1.write(f"\n Kastet sorterat: {dices_sorted}" )
    f1.write(f"\n Antalet femmor: {antal_femmor}" )
        