import random as rnd # Importerar random för att få slumpmässiga punkter till rad 6 och 7

n = 0 # Variabel för hur många punkter som kommer hamna i cirkeln

for k in range(20): # Först gången programmet kör denna rad kod så är k = 0, nästa gång k=1 osv. upp till k=19
    x = rnd.uniform(-1,1) # Eftersom raden har en indentering tillhör den for-satsen
    y = rnd.uniform(-1,1)
    print("(x,y) = (",x,",", y,")" )
    
    if x**2+y**2 <= 1: # Om radien är mindre eller = 1 räknas punkten som inne i cirkeln.
        n += 1 # Plussar på ett för varje punkt som är i cirkeln.
    print(n) # Printar hur många punkter som är innanför cirkeln

print("Antal punkter i cirkeln dividerat med antal simulerade punkter = ",n/(k+1)*4)

# Arean på cirkeln är pi * 1^2 = pi och arean på kvadraten är 2 * 2 = 4
# Alltså är sannolikheten att hamna i cirkeln pi/4 som är cirka 0,78
# Alltså om jag multiplicerar detta tal med fyra får jag pi

