n = 0 # N är en vanlig variabel som används för ett samlingsnamn på nummer/tal

z = int(input("Ange ett startvärde: ")) # Int står för Integer vilket på svenska är heltal.
y = int(input("Ange ett slutvärde: ")) # Användaren får skriva in ett start- och slutvärde.

burr = int(input("Ange multipel för burr: ")) # Användaren får även skriva två multiplar.

birr = int(input("Ange en annan multipel för birr: ")) # Den ena printar burr den andra birr.

for n in range(z,y+1):
    if n % (birr+burr) == 0: # Istället för en multipel så tog jag summan av birr och burr.
        print("Birr burr") # Man skulle även kunna ta differensen mellan birr och burr.

    elif n % burr == 0: # Ett tal divideras med multipeln väljaren väljer och resten blir noll 
        print("Burr") # printas "Burr".

    elif n % birr == 0: # Ett tal divideras med multipeln väljaren väljer och resten blir noll
        print("Birr") # printas "Birr".
    else: # Om inte resten blir noll printas bara talet för sig
        print(n)


