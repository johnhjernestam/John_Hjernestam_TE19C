summa_pengar = int(input("Ange en summa: "))

def antal_lappar(s, k):
    lappar = int(s/k)
    return lappar

def ny_summa(s, k, antal):
    summa = s - (antal * k)
    return summa 

at = antal_lappar(summa_pengar, 1000)
print("Antal tusenlappar: ", at)

ny_total_summa = ny_summa(summa_pengar, 1000, at)
print(ny_total_summa)

af = antal_lappar(ny_total_summa, 500)
print("Antal femhundralappar: ", af)

ny_total_summa = ny_summa(ny_total_summa, 500, af)
print(ny_total_summa)

