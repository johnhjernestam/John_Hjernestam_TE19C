import math # Importerar math för att kunna ta roten ur på rad 3

hypotenusan = math.sqrt(0.5**2+0.5**2) # Räknar ut med pythagoras sats, spelar ingen roll att y-kordinaten 
                                       # är negativ då alla tal upphöjt till 2 blir positivt                   
print(f"{hypotenusan:.5f}") # Printar ut hypotenusan med 5 decimaler vilket är radien från origo