import plotly.express as px # Importerar plotly express
import dash # Importerar dash
import dash_core_components as dcc # Importerar dash core components som dcc 
import dash_html_components as HTML # Importerar dash html components som HTML
import pandas as pd # Importerar pandas som pd
from dash.dependencies import Input, Output # Importerar input och output

# Startar appen
app = dash.Dash(__name__)

# Läser in alla csv filer
df_national = pd.read_csv("CSV_National_Total_Deaths_by_Age_Group.csv") 
df_regional = pd.read_csv("CSV_Regional_Totals_Data.csv")
df_gender = pd.read_csv("CSV_Gender_Data.csv")
df_deaths = pd.read_csv("CSV_National_Daily_Deaths.csv")

fig_deaths = px.line(df_deaths, y="National_Daily_Deaths", x="Date", title="Dagliga dödsfall") # En variabel som sedan används för att representera dagliga dödsfall med plotly express

# Här starat app layouten
app.layout = HTML.Div(children=[

    HTML.H1("Covid-19 data för Sverige", style={'text-align': 'center'}), # Rubriken är på en och samma rad samt centrerad

    dcc.Dropdown( # Dropdown är en mycket förekommande dash component som ger användaren alternativ på vad för typ av data som visas
        id = "drop_national",
        options = [ # Det som står till höger om "the key" label (value) är det användaren ser, det som står till höger om 'value' är det som tas från dataframen
            {'label': 'Antal fall baserat på åldersgrupp', 'value': 'Total_Cases'},
            {'label': 'Antal intensivvårdare baserat på åldersgrupp', 'value': 'Total_ICU_Admissions'},
            {'label': 'Antal dödsfall baserat på åldersgrupp', 'value': 'Total_Deaths'}
        ], #
        value="Total_Cases" # Detta visas först när man kommer in
    ),

    HTML.Br(), # Ger mer plats mellan diven och grafen

    dcc.Graph(id = "graph_national",),

    dcc.Dropdown(
        id = "drop_regional",
        options = [ # Det som står till höger om "the key" label (value) är det användaren ser, det som står till höger om 'value' är det som tas från dataframen
            {'label': 'Antal fall baserat på region', 'value': 'Total_Cases'},
            {'label': 'Antal intensivvårdare baserat på region', 'value': 'Total_ICU_Admissions'},
            {'label': 'Antal dödsfall baserat på region', 'value': 'Total_Deaths'},
            {'label': 'Antal fall per 100 000 invånare', 'value': 'Cases_per_100k_Pop'}
        ], 
        value="Total_Cases" # Detta visas först när man kommer in
    ),

    HTML.Br(), # Ger mer plats mellan diven och grafen

    dcc.Graph(id = "graph_regional",),

    dcc.Dropdown(
        id = "drop_gender",
        options = [ # Det som står till höger om "the key" label (value) är det användaren ser, det som står till höger om 'value' är det som tas från dataframen
            {'label': 'Antal fall baserat på kön', 'value': 'Total_Cases'},
            {'label': 'Antal intensivvårdare baserat på kön', 'value': 'Total_ICU_Admissions'},
            {'label': 'Antal dödsfall baserat på kön', 'value': 'Total_Deaths'},
        ], 
        value="Total_Cases" # Detta visas först när man kommer in
    ),

    HTML.Br(), # Ger mer plats mellan diven och grafen

    dcc.Graph(id = "graph_gender",),

    dcc.Graph(
        id = "graph_deaths",
        figure= fig_deaths,
    ),
]) # Här slutar app layouten

@app.callback( # Callback använder sig av id och komponentens namn (t.ex. children, figure, value) för att kunna koppla ihop delarna
    Output("graph_national", "figure"), # Outputen tar informationen och skickar till där id står och även till dropdown grafen
    [Input("drop_national", "value")] # Inputen åker in dit där det står "value"
)

# Callback-function
def update_figure(value): # Agrumentet value referar alltid till det som står ovanför i inputen, i detta fall "value"
    fig = px.bar(df_national, x="Age_Group", y=value, title=f"{value}") # Först anges vilken dataframe, sedan x och y samt titel
    return fig # Detta kommer ut till outputen


@app.callback( # Callback använder sig av id och komponentens namn (t.ex. children, figure, value)
    Output("graph_regional", "figure"), # Outputen tar informationen och skickar till där id står och även till dropdown grafen
    [Input("drop_regional", "value")] # Inputen åker in dit där det står "value"
)

# Callback-function
def update_figure(value): # Agrumentet value referar alltid till det som står ovanför i inputen, i detta fall "value"
    fig = px.line(df_regional, x="Region", y=value, title=f"{value}") # Först anges vilken dataframe, sedan x och y samt titel
    return fig # Detta kommer ut till outputen


@app.callback( # Callback använder sig av id och komponentens namn (t.ex. children, figure, value)
    Output("graph_gender", "figure"), # Outputen tar informationen och skickar till där id står och även till dropdown grafen
    [Input("drop_gender", "value")] # Inputen åker in dit där det står "value"
)

# Callback-function
def update_figure(value): # Agrumentet value referar alltid till det som står ovanför i inputen, i detta fall "value"
    fig = px.pie(df_gender, values=value, title=f"{value}", names=['män', 'kvinnor']) # Först anges vilken dataframe, sedan x och y samt titel
    return fig # Detta kommer ut till outputen


if __name__ == '__main__': 
    app.run_server(debug=True) # Servern körs
