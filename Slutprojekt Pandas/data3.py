import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("CSV_National_Total_Deaths_by_Age_Group.csv") # Läser in dataframen 

deaths = df['Total_Deaths'] # Tar en del av dataframen och döper delen till deaths detta blir sedan y i grafen

my_labels = df['Age_Group'] # Döper en del av dataframen till my_labels som sedan står för x-titlarna nedanför 
plt.bar(my_labels , deaths)

# Namn för y- och x-axeln osv.
plt.title('Dödstall utifrån ålder')
plt.xlabel('Ålder')
plt.ylabel('Antal')
plt.xticks(rotation=30, fontsize=8)
plt.show()