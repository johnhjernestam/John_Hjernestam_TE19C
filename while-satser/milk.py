bakterier = 1.5e6 # 1.5*10**6
surt = 1e7
faktor = 1.5
h = 0

while bakterier < surt:
    bakterier = faktor*bakterier
    h += 1

print(f"Det tar {h}h i rumstempratur för att mjölken ska surna")