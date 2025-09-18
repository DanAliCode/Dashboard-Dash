from dash import Dash, dcc, html, Input, Output

# Lib de estilização CSS
external_stylesheets =  ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Criando o aplicativo Dash
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Desenvonvendo os options

all_options = {
    'USA': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': ['Montreal', 'Toronto', 'Otawa']
}

# Desenvolvendo o layout
app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'USA',
        id='contries-radio'
    ),
    
    html.Hr(),
    dcc.RadioItems(id='cities-radios'),
    html.Hr(),
    html.Div(id='display-selected-values')
])

# Chamando o callback
@app.callback(
    Output('cities-radios', 'options'),
    Input('contries-radio', 'value'),
)

def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

@app.callback(
    Output('cities-radios', 'value'),
    Input('cities-radios', 'options')
)

def set_cities_value(available_value):
    return available_value[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    Input('contries-radio', 'value'),
    Input('cities-radios', 'value')
)

def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(selected_city, selected_country)

#Função
if __name__ == '__main__':
    app.run(debug=True)