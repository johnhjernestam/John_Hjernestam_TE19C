antal = float(input("Hur många gånger åker du med västtrafik? ")) 

totalKostnad = antal*30

print(f"Totala kostanden är {totalKostnad:.0f}kr")

if antal > 25:
    print("Det är bättre att köpa ett månadskort")
else:
    print(f"Totala kostnaden är {totalKostnad}kr")