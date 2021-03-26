import pandas as pd
import numpy as np

pd.read_csv("Matteprov.csv")

#print(df.head(3))
#print(df.tal1(2))

#print(df.dropna()) # Slänger radenra som innehåller NaN
df = df.fillna(0)
df["Total"] = df.sum(axis=1)
df["Betyg"] = np.where(df["Total"] > 7, "Godkänt", "Underkänt")
