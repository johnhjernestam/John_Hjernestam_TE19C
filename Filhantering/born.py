före1800 = []

with open("Stora forskare.txt", "r") as f1:
    for rad in f1:
        rad = rad.strip("\n") # tar bort radbryningar i början och slutet
        print(rad)
        print(rad[-10:-6])

        år = int(rad[-10:-6])

        if år < 1800:
            före1800.append(rad[0:-11])
print(före1800)

        