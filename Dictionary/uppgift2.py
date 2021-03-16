import random as rnd 

antal_kast = 100000
sidor = 6

kast = {}

for i in range(antal_kast):
    tärnings_kast = rnd.randint(1, sidor)
    
    if tärnings_kast in kast:
        kast[tärnings_kast] += 1
    else:
        kast[tärnings_kast] = 1

for tärnings_kast in range(1, 7):
    print(f"Nummer {tärnings_kast} kastades {kast[tärnings_kast]} gånger.")
