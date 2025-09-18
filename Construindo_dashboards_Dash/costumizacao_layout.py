import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Lib de estilização CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Abrindo aplicação Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Lendo o csv
df = pd.read_csv('../BMW sales data (2010-2024).csv', delimiter=',')


# Criando uma figura com o dataframe
fig = px.bar(df, x='Model', y='Price_USD', color='Region')

##############################################################################

# Configurando o Layout

app_layout = html.Div(id="div1",
    children=[
        html.H1("Hello Dash", id="h1"),
        # html.H1("Hello Dash", id="h1", style={"color": '#b6b6b6'}), # Outro jeito de estilizar diretamente na função
        # Segunda div
        html.Div("Dash: Um framework web para Python"),
        
        dcc.Graph(figure=fig, id="graph")
    ]
)

app.layout = app_layout

if __name__ == '__main__':
    app.run(debug=True)