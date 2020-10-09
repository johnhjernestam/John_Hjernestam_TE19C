fåglar = 8000
antal_år = 0

print(f"År {antal_år}: antal fågöar: {fåglar}st")

while fåglar >= 800:
    fåglar /= 2
    antal_år += 1
    print(f"År {antal_år}: antal fåglar: {fåglar}st")

print(f"Det tar {antal_år} år till fågelpopulationen understiger en tiondel.")