# Jämt eller udda

# Läs in ett tal och checka om talet är jämt eller udda

tal = int(input("Ange ett heltal: ")) #typomvandalr till int (heltal

# modulooperator
#print(tal%2)

# med % --> om tal %2 == 0 --> jämnt, annars udda
if tal%2 == 0:
    print("Talet är jämnt")
else:
    print("Talet är udda")    

