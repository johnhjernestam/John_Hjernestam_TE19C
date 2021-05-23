import pandas as pd # Importerar pandas som pd
import matplotlib.pyplot as plt # Importerar matplotlib som plt

df = pd.read_csv("CSV_Regional_Totals_Data.csv") # Läser in dataframen 

deaths = df['Total_ICU_Admissions'] # Tar en del av dataframen och döper delen till deaths som sedan blir y i grafen

my_labels = df['Region'] # Döper en del av dataframen till my_labels som sedan står för x-titlarna nedanför 
plt.bar(my_labels , deaths, color=['pink', 'purple', 'lightcoral', 'crimson'], width = 0.75) 

# Namn för y- och x-axeln osv.
plt.title('Intensivvårdade')
plt.xlabel('Regioner')
plt.ylabel('Antal')
plt.xticks(rotation=30, fontsize=8)
plt.show()

