tallista = [i for i in range (10)]

print(tallista)

with open("tal.txt", "w") as f:
    # f.write(tallista) går ej att lägga in en lista
    for tal in tallista:
        f.write(f"{tal} ")
