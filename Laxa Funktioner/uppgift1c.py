a1 = int(input("Ange ett startvärde: "))
an = int(input("Ange ett slutvärde: "))
n = an - a1 + 1

def aritmetisk_summa(n, a1, an):
    summa = n*(a1 + an)/2
    return summa
    
s = aritmetisk_summa(n, a1, an)    
print(s)