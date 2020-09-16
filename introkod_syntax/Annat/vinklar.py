vinkel = float(input("Ange en vinkel i grader, där 0 <= v <= 360: "))

# om 0 <= v < 90 spetsig
# rät vinkel v = 90
# trubbig vinkel 90 < v < 180

if vinkel >= 0 and vinkel < 90:
    print("Spetsig vinkel")
elif vinkel == 90:
    print("Rät vinkel")
elif vinkel > 90 and vinkel < 180:
    print("Trubbig vinkel")
else:
    print("Vinkeln är inte spetsig, rät eller trubbig ")