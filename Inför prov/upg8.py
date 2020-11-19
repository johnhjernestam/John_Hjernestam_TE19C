vikt = float(input("Hur mycket väger ditt bagage: "))

längd = float(input("Hur långt är ditt bagage: "))
bredd = float(input("Hur brett är ditt bagage: "))
höjd = float(input("Hur högt är ditt bagage: "))

if vikt > 8:
    print("Bagaget väger för mycket. Ej godkänt!")

elif längd > 55:
    print("För långt. Ej godkänt!")

elif bredd > 40:
    print("För brett.")

elif höjd > 23:
    print("För högt.")
else:
    print("Ditt bagage är godkänt!")




