n = 0 # N är en vanlig variabel som används för ett samlingsnamn på nummer/tal

multipel = float(input("Ange multipel: ")) # Input används för att en användare ska
                                           # kunna välja vilken multipel som den vill.
while n < 100: # När n är mindre 100 så gör den det som är innanför satsen.
    n += 1 # Plussar på ett för varje tal som är mindre än 100.
    
    if n % multipel == 0: # När ett tal divideras med multipeln väljaren väljer och resten blir noll 
        print("Burr") # printas "Burr"
    else: # Om inte resten blir noll printas bara talet för sig
        print(n)