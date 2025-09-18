from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Criando o aplicativo Dash
app = Dash(__name__)

# Criando o DataFrame
df = pd.DataFrame({
    'student_id': range(1,11),
    'score': [1,5,2,5,2,3,1,5,1,5]
})

# Criando o layout
app.layout = html.Div([
    dcc.Dropdown(list(range(1,6)), 1, id='score'),
    'Foi pontuado pelo seguinte quantidade de estudantes',
    html.Div(id='output'),
    dcc.Store(id='store')
])

# Inserindo o dcc.store


# Criando o callback
@app.callback(
    Output('store', 'data'),
    Input('score', 'value')
)
def update_output(value):
    # global df
    # Operação pesada
    filtered_df = df[df["score"] == value]
    # .....
    
    return filtered_df.to_dict()

@app.callback(
    Output('output', 'children'),
    Input('store', 'data')
    )
def updae_output(data):
    filtered_df = pd.DataFrame(data)
    return len(filtered_df)

# Função
if __name__ == '__main__':
    app.run(debug=True)