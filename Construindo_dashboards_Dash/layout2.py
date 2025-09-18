import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Abrindo a aplicação Dash
app = dash.Dash(__name__)

# Lendo o arquivo csv
# df = pd.read_csv('../files/BMW sales data (2010-2024).csv', delimiter=',')


# Montando o layout
app.layout = html.Div([
    html.Label("Dropdown"),
    
    dcc.Dropdown(
        id="dp-1",
        options=[{'label': 'Rio Grande do Sul', 'value': 'RS'},
                 {'label': 'São Paulo', 'value': 'SP'},
                 {'label': 'Parana', 'value': 'PR'}],
        value="RS",  style={"margin-bottom": "120px"}
    ), # Montando um checklist
    html.Label("Checklist"),
    
    dcc.Checklist(
    id="cl-1",
    options=[{'label': 'Rio Grande do Sul', 'value': 'RS'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Parana', 'value': 'PR'}],
    value=["RS"], style={"margin-bottom": "60px"}
    
    ),
    
    html.Label("Text Input"),
    dcc.Input(value='SP', type='text', style={"margin-bottom": "60px"}),
    
    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}' .format(i) if i == 1 else str(i) for i in range(1,10)},
        value=5
    )
    
])



# Runing application
if __name__ == '__main__':
    app.run(debug=True)