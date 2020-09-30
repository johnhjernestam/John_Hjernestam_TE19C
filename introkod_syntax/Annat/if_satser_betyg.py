# x - antal poäng 

# A: $x > 60$

# B: 56-60

# C: 51-55

# D 41-50

# E: 31-40

# F: x <= 30

import random as rnd

poang = rnd.randint(0,65)

klass = ["Kokchun", "Tommy", "Henrik", "Zsofia", "Simon", "Tatiana"]

# print(poang)
# print(klass[5])

if poang > 60:
    betyg = "A"
elif poang <= 60 and poang >= 56:
    betyg = "B"