import dash
from dash import html,dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
# Lendo o arquivo csv 

df = pd.read_csv('../files/gapminder_full.csv', delimiter=',')

# Variavel de estilização css
external_stylesheets =  ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Criando o layout

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

# Plotando grafico com callback
'''
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
'''
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    
    
    fig = px.scatter(
        filtered_df, x="gdp_cap", y="life_exp",
        size="population", color="continent", hover_name="country",
        log_x=True, size_max=55
    )
    
    fig.update_layout(transition_duration=500)
    return fig
    
    

if __name__ == '__main__':
    app.run(debug=True)