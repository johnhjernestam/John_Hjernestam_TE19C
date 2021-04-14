import pandas as pd

df = pd.read_csv("sysselsattning.csv") 

#print(df.columns)
df['Half'] = df['2019'][:12] 

df['Men'] = df['Half'][::2]
print(df['Men'].dropna())

svar = df['Men'].sum(axis=0)
print((f"Under 2019 förvärvsarbetade {svar:.0f} män i Sverige mellan åldrarna 16-44."))



