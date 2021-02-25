mening = input("Skriv en mening: ")

def räkna_ord(text):
    ord = text.split()
    antal_ord = len(ord)
    return antal_ord

print(f"Antal ord i citatet: {räkna_ord(mening)}")  
