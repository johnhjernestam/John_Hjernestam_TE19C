try:
    with open("Stora forskare.txt", "r") as f1:
        for rad in f1:
            print(rad, end="")
except FileNotFoundError:
    print("Filen hittades inte")