grönsaker = ["tomat", "gurka", "majs", "sallad"]
frukter = ["äpple","päron","kiwi", "banan", "jordgubbe", "blåbär"]
fruktsallad = [] # tom lista

# append() - lägger till element i en lista
for grönsak in grönsaker:
    fruktsallad.append(grönsak)

for frukt in frukter:
    fruktsallad.append(frukt)

print(fruktsallad)

