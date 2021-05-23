import pandas as pd # Importerar pandas som pd
import matplotlib.pyplot as plt # Importerar matplotlib som plt

df = pd.read_csv("CSV_Gender_Data.csv") # Läser in dataframen 

value_cases = [df["Total_Cases"][0],df["Total_Cases"][1]] # Tar ut specifik data från csv:en, tar första indexet (alltså 0) och andra (alltså 1)
value_icus = [df["Total_ICU_Admissions"][0],df["Total_ICU_Admissions"][1]] # Tar ut specifik data från csv:en, tar första indexet (alltså 0) och andra (alltså 1)
value_deaths = [df["Total_Deaths"][0],df["Total_Deaths"][1]] # Tar ut specifik data från csv:en, tar första indexet (alltså 0) och andra (alltså 1) från 

def diagram(value, row, column, position, title, labels): # En for loop som minskar antalet rader av kod, loopar igenom värde, rad, kolumn, position, titel och "etiketter"
    plt.subplot(row, column, position)
    plt.pie(value, labels = labels, autopct = '%1.1f%%', startangle=45, shadow = True, colors=['aqua', 'yellow'], explode=(0, 0.125)) # Startangle visar etiketten 45 grader från startposition, shadow=True ger skugga, explode ger utrymme mellan bitarna
    plt.title(title)
    plt.legend() # Visar färg och namn som gör det lätt att förstå vilken bit som betyder vad

diagram(value_cases, 2, 3, 1, "Male- and female cases", ['Male Cases', 'Female Cases']) # 2, 3, 1 står för rad 2, kolumn 3, position 1
diagram(value_icus, 2, 3, 2, "Male- and female ICUs", ['Male ICUs', 'Female ICUs']) # 2, 3, 2 står för rad 2, kolumn 3, position 2
diagram(value_deaths, 2, 3, 3, "Male- and female deaths", ['Male Deaths', 'Female Deaths']) # 2, 3, 3 står för rad 2, kolumn 3, position 3
plt.show() # Här visar den diagramet som skapats