n = 0 # N är en vanlig variabel som används för ett samlingsnamn på nummer/tal

burr = float(input("Ange multipel till burr: ")) # Input används för att en användare ska
                                                 # kunna välja vilken multipel som den vill.
birr = float(input("Ange multipel till birr: ")) # En multipel för burr och en för birr.

while n < 100: # När n är mindre 100 så gör den det som är innanför satsen.
    n = n+1 # Plussar på ett för varje tal som är mindre än 100.

    if n % burr == 0: # När ett tal divideras med multipeln väljaren väljer och resten blir noll 
        print("Burr") # printas "Burr".
    if n % birr == 0: # Samma för den andra multipeln väljaren väljer
        print("Birr") # fast för denna printar den "Birr".
    else: # Om inte resten blir noll printas bara talet för sig
        print(n)



