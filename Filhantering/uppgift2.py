namn = []

with open("Provresultat.txt", "r") as f:
    for item in f:
        namn.append(item)
sorted_list = sorted(namn)


with open("Provresultat.txt", "w") as f:
    for i in sorted_list:
        f.write(f"\n{i}")