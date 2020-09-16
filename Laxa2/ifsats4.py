vinkel = float(input("Ange graderna på din vinkel: "))

if vinkel == 360:
    print("Hel")

elif vinkel > 180:
    print("Konvex")

elif vinkel == 180:
    print("Rak")

elif vinkel > 90:
    print("Trubbig")

elif vinkel < 90:
    print("Spetsig")

elif vinkel == 90:
    print("Rät")









