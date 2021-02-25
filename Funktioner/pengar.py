def växla(summa):
    kontanter = [1000, 500, 200, 100, 50, 20, 10, 5, 1] # sedlar o mynt
    sedlar = ["tusenlappar", "femhundralappar", "tvåhundralappar", "hundralappar", "femtiolappar", "tjugolappar", "tiokronor", "femkronor", "enkronor"] 

    for i in range(len(kontanter)): 
        antal = summa//kontanter[i] # heltalsdivision 
        summa %= kontanter[i] # ger resten vid heltalsdivision per sedel
        print(f"{antal} {sedlar[i]}", end=", ") # skriver ut antal per sedel

växla(5838)