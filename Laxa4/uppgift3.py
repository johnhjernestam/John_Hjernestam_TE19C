summa = 0
n = 0

while n < 100:
    summa = summa + 2**(-n)
    n = n +1

print(f"1+(1/2)+(1/4)+(1/8)+...1/2**n = {summa}")