def växla(summa):
    kontanter = [1000, 500, 200, 100]
    sedlar = ["tusenlapp", "femhundralapp", "tvåhundralapp", "hundralapp"]

    for i in range(len(kontanter)):
        antal_sedlar = summa//kontanter[i]
        summa %= kontanter[i]
        print(f"{antal_sedlar} {sedlar[i]}")
växla(5838) 