import pandas as pd

df = pd.read_csv("sysselsattning.csv") 

#print(df.columns)
df = df['2019'][0:12]
antal_förvärvsarbetare = df.sum().sum()

print(f"Under 2019 förvärvsarbetade {antal_förvärvsarbetare} personer i Sverige mellan åldrarna 16-44.")

import pandas as pd

df = pd.read_csv("sysselsattning.csv")

#print(df.columns)
df = df['2019'][12:24]
antal_ejförvärvsarbetare = df.sum().sum()

print(f"Under 2019 ej förvärvsarbetade {antal_ejförvärvsarbetare} personer i Sverige mellan åldrarna 16-44.")

### HÄR BÖRJAR TÅRTDIAGRAMET ###

import matplotlib.pyplot as plt

min_data = [antal_förvärvsarbetare, antal_ejförvärvsarbetare]

my_labels = 'förvärvsarbetare', 'icke förvärvsarbetare'
my_colors = ['lightblue', 'orange']
my_explode = (0, 0.125)

plt.pie(min_data, labels = my_labels, autopct = '%1.1f%%', startangle=15, shadow = True, colors=my_colors, explode=my_explode)
plt.title("Antal förvärvsarbetare/ej förvärvsarbetare")
plt.show()


