from dash import Dash, dcc, html, callback, Output, Input
import plotly.express as px
import pandas as pd


app = Dash(__name__)

COLOR_MAP = {
    "north": "#1f77b4",
    "south": "#d62728",
    "east": "#2ca02c",
    "west": "#ff7f0e",
}

df = pd.read_csv('https://raw.githubusercontent.com/tonyl15/quantium-starter-repo/refs/heads/main/pink_morsel_sales.csv').sort_values(by='date')
fig = px.line(
    df,
    x="date",
    y="sales",
    line_group="region",
    color="region",
    color_discrete_map=COLOR_MAP,
)

header = html.H1(children='Pink Morsel Sales Over Time')
visualisation = dcc.Graph(
    id='pink-morsel-sales-graph',
    figure=fig
)

# Filtering options for region
region_selector = dcc.RadioItems(
    id='region-selector',
    options=["All", "North", "South", "East", "West"],
    value="All",
    inline=True
)

region_selector_wrapper = html.Div(
  [
    region_selector
  ]
)

@callback(
    Output("pink-morsel-sales-graph", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region.lower()]
    
    updated_fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        line_group="region",
        color="region",
        color_discrete_map=COLOR_MAP,
    )
    return updated_fig

app.layout = html.Div([
    header,
    region_selector_wrapper,
    visualisation
],
    style={
        'width': '80%',
        'margin': '0 auto',
        'textAlign': 'center',
        'fontFamily': 'Arial',
        'padding': '20px'}
)

if __name__ == '__main__':
    app.run(debug=True)
