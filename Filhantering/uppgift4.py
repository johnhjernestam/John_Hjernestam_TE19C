import random as rnd

antal_ettor = 0
antal_tvåor = 0
antal_treor = 0
antal_fyror = 0
antal_femmor = 0
antal_sexor = 0

x = 0

with open("simulering.txt", "x") as f:
    while x < 5:
        x += 1
        for i in range (10**x):
            kast = rnd.randint(1,6)
            if kast == 1:
                antal_ettor += 1
            if kast == 2:
                antal_tvåor += 1
            if kast == 3:
                antal_treor += 1
            if kast == 4:
                antal_fyror += 1
            if kast == 5:
                antal_femmor += 1
            if kast == 6:
                antal_sexor += 1

        sannolikhet_ettor = antal_ettor/(10**x)
        sannolikhet_tvåor = antal_tvåor/(10**x)
        sannolikhet_treor = antal_treor/(10**x)
        sannolikhet_fyror = antal_fyror/(10**x)
        sannolikhet_femmor = antal_femmor/(10**x)
        sannolikhet_sexor = antal_sexor/(10**x)

        f.write(f"\nAntal tärningskast: {10**x} \nAntal ettor = {antal_ettor}, sannolikhet {sannolikhet_ettor} \nAntal tvaor = {antal_tvåor} , sannolikhet {sannolikhet_tvåor} \nAntal treor = {antal_treor}, sannolikhet {sannolikhet_treor} \nAntal fyror = {antal_fyror}, sannolikhet {sannolikhet_fyror} \nAntal femmor = {antal_femmor}, sannolikhet {sannolikhet_femmor} \nAntal Sexor = {antal_sexor}, sannolikhet {sannolikhet_sexor}")
        f.write(f"\n")
        



    
