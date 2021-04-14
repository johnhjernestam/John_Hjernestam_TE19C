import pandas as pd 

df = pd.read_csv("sysselsattning.csv") 

#print(df.columns)
df['Half'] = df['2019'][:12] # Män som förvärvsarbetar

df['Men'] = df['Half'][::2]
print(df['Men'].dropna())

svar1 = df['Men'].sum(axis=0)
#print((f"Under 2019 förvärvsarbetade {svar:.0f} män i Sverige mellan åldrarna 16-44."))

import pandas as pd

df = pd.read_csv("sysselsattning.csv") 

#print(df.columns)
df['Half'] = df['2019'][:12] # Kvinnor som förvärvsarbetar 

df['Women'] = df['Half'][1::2]
print(df['Women'].dropna())

svar2 = df['Women'].sum(axis=0)
#print((f"Under 2019 förvärvsarbetade {svar:.0f} kvinnor i Sverige mellan åldrarna 16-44."))

import pandas as pd

df = pd.read_csv("sysselsattning.csv") # Män som inte förvärvsarbetar (lägg till inte)

#print(df.columns)
df['Half'] = df['2019'][12:] 

df['Men'] = df['Half'][::2]
print(df['Men'].dropna())

svar3 = df['Men'].sum(axis=0)
#print((f"Under 2019 förvärvsarbetade inte {svar:.0f} män i Sverige mellan åldrarna 16-44."))

import pandas as pd

df = pd.read_csv("sysselsattning.csv") 

#print(df.columns)
df['Half'] = df['2019'][12:] # Kvinnor som inte förvärvsarbetar (lägg till inte)

df['Women'] = df['Half'][1::2]
print(df['Women'].dropna())

svar4 = df['Women'].sum(axis=0)
#print((f"Under 2019 förvärvsarbetade {svar:.0f} kvinnor i Sverige mellan åldrarna 16-44."))

# Datavisualisering
import matplotlib.pyplot as plt

sysselsättningar = ['M förvärvs...', 'K förvärvs...', 'M ej förvärvs...', 'K ej förvärvs...']
svar = [svar1, svar2, svar3, svar4]

plt.bar(sysselsättningar , svar, width = 0.4)

# Namn för y- och x-axeln osv.
plt.title('Förvärvsarbetare')
plt.xlabel('sysselsättningar')
plt.ylabel('Antal')
plt.show()











