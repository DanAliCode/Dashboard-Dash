from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Construindo o app dash
app = Dash(__name__)

# Lendo o arquivo csv
df = pd.read_csv('../files/gapminder_full.csv', delimiter=',')

# Desenvolvendo o layout

app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value='Montréal'),
    dcc.Input(id='input-2', type='text', value='Canada'),
    html.Div(id='number-output')
])

# Criando o callback
@app.callback(
    Output("number-output", "children"),
    Input("input-1", "value"),
    Input("input-2", "value")
)

def update_output(input1, input2):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1,input2)

#Função
if __name__ == '__main__':
    app.run(debug=True)