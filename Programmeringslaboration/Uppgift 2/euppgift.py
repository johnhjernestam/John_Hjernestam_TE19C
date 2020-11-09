n = 0
z = int(input("Ange ett startvärde: ")) # Int står för Integer vilket på svenska är heltal.
y = int(input("Ange ett slutvärde: ")) # Användaren får skriva in ett start- och slutvärde.

burr = int(input("Ange multipel för burr: ")) # Användaren får även skriva två multiplar.

birr = int(input("Ange en annan multipel för birr: ")) # Den ena printar burr den andra birr.

# Z är variabeln för startvärdet och y är variabeln för slutvärdet. Eftersom slutvärdet alltid subtraheras
for n in range(z,y+1): # med 1 in range så plussar jag på 1 för att få talet användaren skrev in.
    if n % (birr*burr) == 0: # Ett tal divideras med båda multiplarna 
        print("Birr burr") # väljaren väljer och om resten blir noll printas Birr Burr.

    elif n % burr == 0: # Ett tal divideras med multipeln väljaren väljer och resten blir noll 
        print("Burr") # printas "Burr".

    elif n % birr == 0: # Ett tal divideras med multipeln väljaren väljer och resten blir noll 
        print("Birr") # printas "Birr".
    else: # Om inte resten blir noll printas bara talet för sig
        print(n)