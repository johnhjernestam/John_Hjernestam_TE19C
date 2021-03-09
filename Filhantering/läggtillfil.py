with open("Stora forskare.txt", "r") as f1, open ("Stora forskare 2.txt", "w") as f2:
    for rad in f1:
        rad = rad.strip(" ")
        f2.write(rad)

    f2.write("Andreas Wiles 1953-04-11\n")