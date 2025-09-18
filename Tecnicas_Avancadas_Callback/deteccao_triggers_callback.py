import dash
from dash import html, dcc, Input, Output, callback_context

# Criando o aplicativo Dash
app = dash.Dash(__name__)

# Criando o layout
app.layout = html.Div([
    html.Button('Button 1', id='btn-1-ctx-example'),
    html.Button('Buttton 2', id='btn-2-ctx-example'),
    html.Button('Button 3', id='btn-3-ctx-example'),
    html.Div(id='container-ctx-example')
])

#Criando o callback
@app.callback(
    Output('container-ctx-example', 'children'),
    Input('btn-1-ctx-example', 'n_clicks'),
    Input('btn-2-ctx-example', 'n_clicks'),
    Input('btn-3-ctx-example', 'n_clicks')
)

def display(btn1,btn2,btn3):
    # import pdb
    # pdb.set_trace()
    id_triggered = callback_context.triggered[0]['prop_id'].split('.')[0]
    
    return id_triggered

#Função
if __name__ == '__main__':
    app.run(debug=True)