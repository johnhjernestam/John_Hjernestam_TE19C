summa_pengar = int(input("Ange en summa: "))

tusen_lappar = int(summa_pengar/1000)
print(tusen_lappar)

efter_tusen_lappar = summa_pengar - tusen_lappar*1000
print(efter_tusen_lappar)

femhundra_lappar = int(efter_tusen_lappar/500)
print(femhundra_lappar)

efter_femhundra_lappar = efter_tusen_lappar - femhundra_lappar*500
print(efter_femhundra_lappar)
    
tvåhundra_lappar = int(efter_femhundra_lappar/200)
print(tvåhundra_lappar)

efter_tvåhundra_lappar = efter_femhundra_lappar - tvåhundra_lappar*200
print(efter_tvåhundra_lappar)

hundra_lappar = int(efter_tvåhundra_lappar/100)
print(hundra_lappar)

efter_hundra_lappar = efter_tvåhundra_lappar - hundra_lappar*100
print(efter_hundra_lappar)

