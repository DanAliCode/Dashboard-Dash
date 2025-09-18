from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd

# Construindo o app dash
app = Dash(__name__)

# Lendo o arquivo csv
df = pd.read_csv('../files/gapminder_full.csv', delimiter=',')

# Desenvolvendo o layout

app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value='Montreal'),
    dcc.Input(id='input-2', type='text', value='Canada'),
    html.Button(id='submit-button-state', children='Submit'),
    html.Div(id='number-output'),
])

# Criando o callback
@app.callback(
    Output("number-output", "children"),
    Input('submit-button-state', 'n_clicks'),
    State("input-1", "value"),
    State("input-2", "value")
)


def update_output(input1, input2, n_clicks):
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1,input2)

#Função
if __name__ == '__main__':
    app.run(debug=True)