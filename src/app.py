from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("data/clean/movies_clean_df.csv", index_col=0)
genres = sorted(list(set(df["Major Genre"])))


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='ycol', 
                value='Running Time min',
                options=[{'label': i, 'value': i} for i in df.columns])),
        dbc.Col([html.Iframe(
            id='scatter',
            style={'border-width':'0', 'width':'100%', 'height':'400px'}),
        dcc.Slider(id='xslider', min=2, max=10),]),
        ])
    ])])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'),
    Input('ycol', 'value')
)
def plot_altairs(xmax, ycol, df=df.copy()):
    chart = alt.Chart(df[df['IMDB Rating'] < xmax]).mark_point().encode(
        x='IMDB Rating',
        y=ycol,
        color="Major Genre",
        tooltip=['IMDB Rating:N']).interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)