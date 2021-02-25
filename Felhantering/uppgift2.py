def ar_fyrsiffrigt(tal):
    if tal//1000 >= 1 and tal//1000 < 10 or tal//1000 < 0:
        return True
    else:
        return False

# testprogram
testtal = [100,231,10000,10001, -1000, 102313]

for t in testtal:
    if ar_fyrsiffrigt(t):
        print(f"{t} är fyrsiffrigt")
    else:
        print(f"{t} är inte fyrsiffrigt")