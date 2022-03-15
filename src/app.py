from tkinter.ttk import Style
from dash import Dash, html, dcc, Input, Output, State
import altair as alt
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("../data/clean/movies_clean_df.csv", index_col=0).rename(
    columns={'Major Genre': 'Major_genre',  
    'IMDB Rating': 'IMDB_rating', 'Running Time min': 'Duration'}, inplace=False)

genre = sorted(list(df["Major_genre"].dropna().unique()))
year = sorted(list(df["Year"].dropna().astype(str).unique()))
default_genres = ["Action", "Adventure", "Comedy", "Drama", "Horror", "Romantic Comedy"]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Movie lover"
server = app.server

app.layout = dbc.Container([
    dbc.Row(
        #Title
        html.Div([
            html.Pre(
                children="Movie Lover",
                style={"text-aligh":"left", "font-size":"300%", "color":"black", 'margin-left': '0px'}
            ),
            html.P(
                "An Interactive Movie Information Dashboard", 
                style={'color': '#20314a', 'fontSize': 17, 'text-align':'left', 'fontStyle':'italic' }
            )
            ],
        style={"backgroundColor": "#b1d0fc"})
        ),
        html.Br(),
    dbc.Row([
        dbc.Col(),
        dbc.Col([
        dbc.Button(
                "Tips", id='popover-target', color = 'secondary', size="md"
            ),
            dbc.Popover(
                [
                    dbc.PopoverHeader('plot interactions:'),
                    dbc.PopoverBody(
                        dcc.Markdown(
                    """
                        1. Hover over the scatter points to see detailed rating values and duration.
                        2. Click on any of the bar to see highlighted information of a genre.
                        3. Click on the white area in the bar plot to exit the highlight mode.
                        4. Click and drag on the line plot to create movable selection region.
                        5. Click on the white area in the line plot to disregard the selected region"""
                    ))
                ],
                id = 'popover',
                target='popover-target',
                placement='bottom',
                is_open=False
            )], width=1),
    ]),
    html.Br(),
   dbc.Row([
       #first column with narrower width
       dbc.Col([
           #Slider and checklist
           dbc.Card([
               dbc.CardHeader(
                   html.Label("Movie Criterions",
                   style={"font-size":17})),
               dbc.CardBody([
                   dcc.Loading([
           html.Div(
               html.P("Year range"),
                style={'text_aligh': 'left', 'color': '#0f3c63', 'font-family': 'sans-serif'}),
           html.Br(),
           dcc.RangeSlider(
               className="slider_class",
                id="year_range",
                count=1,
                step=1,
                min=1980,
                max=2016,
                value=[1990, 2005],
                tooltip={"placement": "bottom", "always_visible": True},
                marks={1980: {"label": "1980"}, 2016: {"label": "2016"}}
                ),
            #break between slider and checklist
            html.Br(),
            html.Br(),
            html.Div(html.P("Select the movie genre"),
            style={'text_aligh': 'left', 'color': '#0f3c63', 'font-family': 'sans-serif'}),
            dcc.Checklist(
                id="genre_checklist",                    
                className="genre-container",
                inputClassName="genre-input",
                labelClassName="genre-label",
                options=[{"label": i, "value": i} for i in genre],                        
                value=default_genres,
                labelStyle={"display":"block",
                            "margin-left": "30px"}),
            html.Br(),
            html.Hr(),
            html.Div([
        html.P("About:", style={'text_aligh': 'left', 'color': 'charcol', 'font-family': 'sans-serif'}), 
        dcc.Markdown("Contributors of this dashboard: Adrianne Leung, Linhan Cai, Junrong Zhu, Zack Tang. The source code can be found [Here](https://github.com/UBC-MDS/movielover_py/blob/main/src/app.py). Detailed information about wrangled data, dashboard purpose and how to contribution can be retrieved from Github [repository](https://github.com/UBC-MDS/movielover_py). The original dataset is from [Vega Dataset](https://github.com/vega/vega-datasets).",
        style={'color': 'charcol', 'fontSize': 14, 'text-align':'left'})
            ])
            ])
            ])
            ])
        ], width=3),
    html.Br(), 
    #second column
    dbc.Col(
        html.Iframe(
            #three plots 
            id="plot_graphs",
            style={"display": "block",
                    "margin": "auto",
                    "overflow": " hidden", 
                    "width" : "300%", "height":"800px"}
        ),
        )
        ]),
])


@app.callback(
    Output('plot_graphs', 'srcDoc'),
    Input('genre_checklist', 'value'),
    Input('year_range', 'value')
)

#plotting function
def plot_graphs(genre, year_range):
    filter_genre = df[df.Major_genre.isin(genre)]

    filter_data = filter_genre.query("Year >= @year_range[0] & Year <= @year_range[1] & Major_genre in @genre").dropna()
    brush = alt.selection_interval()
    click = alt.selection_multi(fields=['Major_genre'])

    scatter = alt.Chart(filter_data, title="IMDB Rating Vs. Duration (in mins)").mark_circle(opacity=0.3).encode(
        x=alt.Y("IMDB_rating", title="IMDB Rating"),
        y=alt.X("Duration", title="Duration (in mins)"),
        color=alt.condition(brush, 'Major_genre', alt.value('lightgray')),
        tooltip=alt.Tooltip(["IMDB_rating", "Duration"]),
        opacity=alt.condition(click, alt.value(0.9), alt.value(0.1))).add_selection(brush).properties(
        width=350,
        height=320
    )

    bar = alt.Chart(filter_data, title='Gross Revenue By Genre (box office)').mark_bar().encode(
        x=alt.X('sum(US_Revenue)', axis=alt.Axis(title='Gross Revenue (in millions USD)')),
        y=alt.Y('Major_genre', axis=alt.Axis(title='Major Genre')),
        color=alt.Color('Major_genre', legend=alt.Legend(title='Genres')))

    barplot = bar.encode(opacity=alt.condition(click, alt.value(0.9), alt.value(0.1)),
       tooltip=alt.Tooltip('sum(US_Revenue)', format="$,.0f")).add_selection(click).properties(
        width=350,
        height=320

    )

    line = alt.Chart(filter_data, title="Average Revenue By Genre (box office)").mark_line(point=True).encode(
        y=alt.Y("mean(US_Revenue)", axis=alt.Axis(title='Average Revenue (in millions USD)', format='$.0f')),
        x=alt.X("Year", axis=alt.Axis(title="Year", format='.0f')),
        color=alt.condition(brush, 'Major_genre', alt.value('lightgray')),
        tooltip=alt.Tooltip('mean(US_Revenue)', format="$,.0f"),
        opacity=alt.condition(click, alt.value(0.9), alt.value(0.1))).add_selection(brush).properties(
        width=800,
        height=320
    )

    chart = ((scatter | barplot) & line).configure_axis(
        labelFontSize=12, 
        titleFontSize=14).configure_legend(
            titleFontSize=16
            ).configure_title(
                fontSize= 20)

    return chart.to_html()

#callback for popover
@app.callback(
    Output('popover', 'is_open'),
    [Input('popover-target', 'n_clicks')],
    [State('popover', 'is_open')]
    )

#popoverfunction
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)
