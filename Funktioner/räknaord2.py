citat = "I stand on the shoulders of giants"

def räkna_ord(text):
    ord = text.split()
    antal_ord = len(ord)
    return antal_ord

print(f"Antal ord i citatet: {räkna_ord(citat)}")
