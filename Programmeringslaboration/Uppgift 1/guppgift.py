import random as rnd # Importerar random för att få slumpmässiga punkter till rad 12 och 13
import matplotlib.pyplot as plt # Importerar matplotlib för att kunna rita ut ett diagram på rad 23-30

n = 0

xinne = [] # En list för x-värdena då x är inne i cirkeln
yinne = [] # En list för y-värdena då x är inne i cirkeln
xutan =[] # En list för x-värdena då x är utanför cirkeln
yutan = [] # En list för x-värdena då y är utanför cirkeln

for k in range(100000): # Först gången programmet kör denna rad kod så är k = 0, nästa gång k=1 osv. upp till k=100000
    x = rnd.uniform(-1,1) # Eftersom raden har en indentering tillhör den for-satsen.
    y = rnd.uniform(-1,1)
    #print("(x,y) = (",x,",", y,")" )
    if x**2+y**2 <= 1: # Om radien är mindre eller = 1 räknas punkten som inne i cirkeln.
        n += 1 # Plussar på ett för varje punkt som är i cirkeln.
        xinne.append(x) # Append används för att lägga saker i en lista som finns.
        yinne.append(y) # Punkterna som är innanför cirkeln.
    else:
        xutan.append(x) # Här är punkterna som inte är innanför cirkeln då radien
        yutan.append(y) # för dessa punkter från origo är större än 1.

plt.ylim(-1,1) # En gräns för hur stort y får vara i diagramet. Y ska vara mellan -1 och 1.
plt.xlim(-1,1) # En gräns för hur stort x får vara i diagramet. X ska vara mellan -1 och 1.

plt.ylabel("y-axel")
plt.xlabel("x-axel")
plt.title("Pilkastning")

plt.plot(xinne, yinne,"*m") # Ritar ut punkterna som är innaför cirkeln med stjärnor i färgen magenta
                            # * står för stjärna och m står för magenta
plt.plot(xutan, yutan,"*k") # Ritar ut punkterna som är innaför cirkeln med stjärnor i färgen svart
                            # * står för stjärna och k står för svart
plt.show() # Visar diagramet som programmet körde 