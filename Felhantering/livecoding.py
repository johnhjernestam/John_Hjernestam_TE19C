# låt användaren mata in ett antal tal
# Skriv ut största talet 
# Skriv ut minsta talet

tal_str = input("Skriv in ett antal tal med mellanrum emellan: ")
lista_str = tal_str.split() # Split ger oss en lista

try:
    tal_lista = [float(x) for x in lista_str]
    störst = max(tal_lista)
    minst = min(tal_lista)
except:
    print("Felaktiga tal")

print(tal_lista)