import numpy as np 
import random as rnd 

utfall = np.zeros(6, dtype=int)

antal_kast = 100000

for i in range(antal_kast):
    kast = rnd.randint(1,6)
    utfall[kast-1] += 1

print(f"Tärningskast: {utfall}")
print(f"Sannolikhet: {utfall/antal_kast}") 