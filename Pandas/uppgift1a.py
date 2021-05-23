import pandas as pd

df = pd.read_csv("sysselsattning.csv") # (SIDENOTE) Behövde ta bort översta raden för det funkade inte/blev fult när den var med

print(df.columns)
df = df['2019'][0:12]
antal_förvärvsarbetare = df.sum().sum()

print(f"Under 2019 förvärvsarbetade {antal_förvärvsarbetare} personer i Sverige mellan åldrarna 16-44.")