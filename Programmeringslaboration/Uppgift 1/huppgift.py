import random as rnd # Importerar random för att få slumpmässiga punkter till rad 6 och 7

n = 0 # Variabel för hur många punkter som kommer hamna i cirkeln

for k in range(100): # Först gången programmet kör denna rad kod så är k = 0, nästa gång k=1 osv. upp till k=99
    x = rnd.uniform(-0.5,0.5) # Jag hittar sambandet att cirklens radie är 1 i uppgiftens exempel
    y = rnd.uniform(-0.5,0.5) # och när jag byter den till något som 0.5 tex så fungerar det likadant
    print("(x,y) = (",x,",", y,")" ) # om punkten är innanför. 
    
    if x**2+y**2 <= 0.25: # Om radien är mindre eller = 0.25 räknas punkten som inne i cirkeln.
        n += 1 # Plussar på ett för varje punkt som är i cirkeln.
    print(n) # Printar hur många punkter som är innanför cirkeln

print("Antal punkter i cirkeln dividerat med antal simulerade punkter = ",n/(k+1)*100,"%") 
# Räknar ut hur många procent av punkterna som hamnar i cirkeln genom att ta n (vilket är antal punkter som
# hamnar i cirkeln) delat med k+1 (k är nitton vilket är varför + 1 är med då det är tjugo punkter) och till
# sist gånger 100 för att få i svaret i procentenheter.
