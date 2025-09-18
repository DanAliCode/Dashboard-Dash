import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('../files/BMW sales data (2010-2024).csv', delimiter=',')


# Criando uma figura com o dataframe
fig = px.bar(df, x='Model', y='Price_USD', color='Region')

##############################################################################

# Configurando o Layout

app_layout = html.Div(id="div1",
    children=[
        html.H1("Hello Dash", id="h1"),
        # Segunda div
        html.Div("Dash: Um framework web para Python"),
        
        dcc.Graph(figure=fig, id="graph")
    ]
)

app.layout = app_layout

if __name__ == '__main__':
    app.run(debug=True)