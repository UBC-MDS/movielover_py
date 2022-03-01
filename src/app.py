from dash import Dash, html, dcc, Input, Output
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("data/clean/movies_clean_df.csv", index_col=0).rename(
    columns={'Major Genre': 'Major_genre', 'Year': 'Year'}, inplace=False)
# genres = sorted(list(set(df["Major Genre"])))
genre = sorted(list(df["Major_genre"].dropna().unique()))
year = sorted(list(df["Year"].dropna().astype(str).unique()))

default_genres = ["Action", "Adventure", "Comedy", "Drama", "Horror", "Romantic Comedy"]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# app.layout = dbc.Container([
#     html.Div([
#     dbc.Row([
#         dbc.Col(
#             dcc.Dropdown(
#                 id='ycol', 
#                 value='Running Time min',
#                 options=[{'label': i, 'value': i} for i in df.columns])),
#         dbc.Col([html.Iframe(
#             id='scatter',
#             style={'border-width':'0', 'width':'100%', 'height':'400px'}),
#         dcc.Slider(id='xslider', min=2, max=10),]),
#         ])
#     ])])

# @app.callback(
#     Output('scatter', 'srcDoc'),
#     Input('xslider', 'value'),
#     Input('ycol', 'value')
# )
# def plot_altairs(xmax, ycol, df=df.copy()):
#     chart = alt.Chart(df[df['IMDB Rating'] < xmax]).mark_point().encode(
#         x='IMDB Rating',
#         y=ycol,
#         color="Major Genre",
#         tooltip=['IMDB Rating:N']).interactive()
#     return chart.to_html()

@app.callback(
    Output('barchart', 'srcDoc'),
    Input('genre_cb', 'value'),
    Input('year_range', 'value')
)
def plot_bar(genre, year_range):
    filter_genre = df[df.Major_genre.isin(genre)]
    
    filter_data = filter_genre.query("Year >= @year_range[0] & Year <= @year_range[1] & Major_genre in @genre").dropna()

    click = alt.selection_multi(fields=['Major_genre'])
    bar = alt.Chart(filter_data, title='Gross revenue (box office) by genre').mark_bar().encode(
        x=alt.X('Major_genre', axis=alt.Axis(title='Major genre')),
        y=alt.Y('sum(US_Revenue)', axis=alt.Axis(title='Gross Revenue (in millions USD)')),
        color=alt.Color('Major_genre', legend=None))

    barplot = bar.encode(opacity=alt.condition(click, alt.value(0.9), alt.value(0.1)),
       tooltip=alt.Tooltip('sum(US_Revenue)', format="$,.0f")).add_selection(click)
    chart = barplot
    return chart.to_html()

app.layout = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col([
                dcc.Checklist(
                    id="genre_cb",
                    className="app-main--genre-cb-container",
                    inputClassName="app-main--cb-input",
                    labelClassName="app-main--cb-label",
                    options=[{"label": g, "value": g} for g in genre],
                    value=default_genres
                ),
                dcc.RangeSlider(
                            className="slider_class",
                            id="year_range",
                            count=1,
                            step=1,
                            min=df["Year"].min(),
                            max=df["Year"].max(),
                            value=[2000, 2005],
                            marks={
                                1980: {
                                    "label": "1980",
                                },
                                2021: {"label": "2021"},
                            },
                            tooltip={"always_visible": False, "placement": "top"},
                        ),]),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader(
                                    [
                                        html.Label(
                                            "xxx".upper(),
                                            style={"font-size": 17},
                                        ),
                                        
                                    ]
                                ),
                                dbc.CardBody(
                                    [
                                        dcc.Loading(
                                            html.Iframe(
                                                id="barchart",
                                                style={
                                                    "display": "block",
                                                    "overflow": " hidden",
                                                    "margin": "auto",
                                                    "border-width": "0",
                                                    "width": "1550px",
                                                    "height": "500px",
                                                },
                                            ),
                                        )
                                    ]
                                ),
                            ],
                            style={
                                "height": "100%",
                                "margin-left": "15px",
                                "background": "#f0f0f0",
                            },
                        )
                    ])
            ])
    ])])

if __name__ == '__main__':
    app.run_server(debug=True)