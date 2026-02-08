from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash()

df = pd.read_csv('https://raw.githubusercontent.com/tonyl15/quantium-starter-repo/refs/heads/main/pink_morsel_sales.csv').sort_values(by='date')

fig = px.line(df, x="date", y="sales", title='Pink Morsel Sales Over Time')

app.layout = html.Div([
    html.H1(children='Pink Morsel Sales Over Time'),
    
    dcc.Graph(
        id='pink-morsel-sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
