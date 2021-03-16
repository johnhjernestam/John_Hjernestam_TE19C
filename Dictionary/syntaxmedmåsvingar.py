glosor = {
    "tilldela":"ge ett värde till en variabel", 
    "datastruktur":"strukturering av data", 
    "sträng":"sekvens av tecken"
}

# lägga till ett element
glosor["dictionary"] = "datastruktur för att spara data i key:value par"

#print(glosor["tilldela"])
#print(glosor["sträng"])
#print(glosor["dictionary"])

print("Ord vi behöver lära oss: ")
# Ett sätt att loopa igenom en dictionary
for key in glosor:
    print(f"{key} \t {glosor[key]}")

#ett annat sätt 
for key, value in glosor.items():
    print(f"{key} \t {value}")
