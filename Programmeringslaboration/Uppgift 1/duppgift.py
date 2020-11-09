import random as rnd # Importerar random för att få slumpmässiga punkter till rad 4 och 5

for k in range(20):  # Första gången programmet kör denna rad kod så är k = 0, nästa gång k=1 osv. upp till k=19
    x = rnd.uniform(-1,1)  # Eftersom raden har en indentering tillhör den for-satsen
    y = rnd.uniform(-1,1) 
    print("(x,y) = (",x,",", y,")" ) # Efter k har gått igenom printar den ut en slumpmässig punkt.
                                     # Detta upprepas 19 gånger till. X och y printas ut.




 
