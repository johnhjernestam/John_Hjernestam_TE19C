import pandas as pd

df = pd.read_csv("sysselsattning.csv") 

#print(df.columns)
df['Half'] = df['2019'][12:] 

df['Women'] = df['Half'][1::2]
print(df['Women'].dropna())

svar = df['Women'].sum(axis=0)
print((f"Under 2019 förvärvsarbetade {svar:.0f} kvinnor i Sverige mellan åldrarna 16-44."))






