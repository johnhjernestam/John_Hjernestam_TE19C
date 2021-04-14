import pandas as pd

df = pd.read_csv("sysselsattning.csv")

#print(df.columns)
df = df['2019'][12:24]
antal_ejförvärvsarbetare = df.sum().sum()

print(f"Under 2019 ej förvärvsarbetade {antal_ejförvärvsarbetare} personer i Sverige mellan åldrarna 16-44.")




