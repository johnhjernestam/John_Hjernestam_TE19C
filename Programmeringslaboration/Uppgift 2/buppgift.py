n = 0 # N är en vanlig variabel som används för ett samlingsnamn på nummer/tal

while n < 100: # När n är mindre 100 så gör den det som är innanför satsen.
    n = n+1 # Plussar på ett för varje tal som är mindre än 100.

    if n % 5 == 0: # När ett tal divideras med 5 och 
        print("Burr") # resten blir noll printas "Burr"
    else: # Om inte resten blir noll printas bara talet för sig
        print(n)


