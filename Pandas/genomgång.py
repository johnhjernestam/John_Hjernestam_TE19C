import pandas as pd
import numpy as np

df = pd.read_csv("Matteprov.csv")

#print(df.head(3))
#print(df.tal1(2))

#print(df.dropna()) # Slänger raderna som innehåller NaN 
df = df.fillna(0)
df["Total"] = df.sum(axis=1)
df["Betyg"] = np.where(df["Total"] > 7, "Godkänt", "Underkänt")

# Conditional Filtering - villkorlog sökning (filtrering)
df_G = df[df["Betyg"]=="Godkänt"]
df_U = df[df["Betyg"]=="Godkänt"]

# Datavisualisering
import matplotlib.pyplot as plt

betygsLista = df["Betyg"].value_counts().tolist()
labels = df["Betyg"].unique()

plt.bar(labels, betygsLista, width = 0.4, color = ["green", "orange"])
plt.title("Antal godkända/underkända i klassen")
plt.show()
